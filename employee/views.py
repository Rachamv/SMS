from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from reportlab.pdfgen import canvas
from io import BytesIO
from attendance.models import EmployeeAttendance

from .models import (
    LeaveRequest,
    EducationInfo,
    TrainingInfo,
    EmployeeJobInfo,
    ExperienceInfo,
    EmployeeInfo,
    EmployeeDocument,
)
from .forms import LeaveRequestForm, EmployeeReportForm, ProfileUpdateForm

class EmployeeDetailView(LoginRequiredMixin, View):
    def get(self, request, employee_id):
        employee = get_object_or_404(EmployeeInfo, id=employee_id)
        education_info = EducationInfo.objects.filter(personal_info=employee)
        training_info = TrainingInfo.objects.filter(personal_info=employee)
        job_info = EmployeeJobInfo.objects.get(personal_info=employee)
        experience_info = ExperienceInfo.objects.filter(personal_info=employee)

        context = {
            'employee': employee,
            'education_info': education_info,
            'training_info': training_info,
            'job_info': job_info,
            'experience_info': experience_info,
        }

        return render(request, 'employee/employee_detail.html', context)

    def post(self, request, employee_id):
        employee = get_object_or_404(EmployeeInfo, id=employee_id)
        form = ProfileUpdateForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee:employee_detail', employee_id=employee_id)

        context = {
            'employee': employee,
            'form': form,
        }
        return render(request, 'employee/employee_detail.html', context)


@login_required
def leave_request(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.employee = request.user.employeejobinfo

            if request.user.groups.filter(name__in=['ChiefExecutive', 'Director']).exists():
                leave_request.status = 'approved'
            else:
                leave_request.status = 'pending'

            leave_request.save()
            messages.success(request, 'Leave request submitted successfully.')
            return redirect('employee:leave_request_success')
    else:
        form = LeaveRequestForm()

    context = {'form': form}
    return render(request, 'employee/leave_request.html', context)


@login_required
def employee_report(request):
    if request.method == 'POST':
        form = EmployeeReportForm(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data['employee_id']
            employee = get_object_or_404(EmployeeInfo, id=employee_id)
            job_info = EmployeeJobInfo.objects.get(personal_info=employee)
            attendance_history = EmployeeAttendance.objects.filter(employee=job_info)

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="employee_report.pdf"'

            buffer = BytesIO()
            pdf = canvas.Canvas(buffer)

            pdf.setFont('Helvetica-Bold', 16)
            pdf.drawString(50, 750, 'Employee Report')
            pdf.setFont('Helvetica-Bold', 12)
            pdf.drawString(50, 700, f'Employee Name: {employee.name}')
            pdf.drawString(50, 680, f'Designation: {job_info.designation}')
            pdf.drawString(50, 660, f'Department: {job_info.department.name}')

            pdf.setFont('Helvetica-Bold', 14)
            pdf.drawString(50, 600, 'Attendance History')

            y = 570
            for attendance in attendance_history:
                date = attendance.date.strftime('%Y-%m-%d')
                status = attendance.get_status_display()
                pdf.drawString(50, y, f'{date}: {status}')
                y -= 20

            pdf.showPage()
            pdf.save()

            pdf_data = buffer.getvalue()
            buffer.close()
            response.write(pdf_data)

            return response
    else:
        form = EmployeeReportForm()

    context = {'form': form}
    return render(request, 'employee/employee_report.html', context)


@login_required
def upload_document(request):
    if request.method == 'POST':
        form = EmployeeDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.employee = request.user.employeejobinfo
            document.save()
            messages.success(request, 'Document uploaded successfully.')
            return redirect('employee:document_list')
    else:
        form = EmployeeDocumentForm()

    context = {'form': form}
    return render(request, 'employee/upload_document.html', context)


@login_required
def document_list(request):
    documents = EmployeeDocument.objects.filter(employee=request.user.employeejobinfo)
    context = {'documents': documents}
    return render(request, 'employee/document_list.html', context)
