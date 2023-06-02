from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Period, StudentAttendance, EmployeeAttendance
from .forms import AttendanceForm, AttendanceSearchForm, BulkAttendanceForm
from student.models import EnrolledStudent

@login_required
def mark_student_attendance(request, class_name, student_id):
    student = get_object_or_404(EnrolledStudent, id=student_id)
    if request.user != student.class_name.teacher:
        return redirect('attendance:attendance-list')  # Redirect to the attendance list if user is not the student's teacher

    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            period = form.cleaned_data['period']
            attendance_status = form.cleaned_data['status']
            std_attendance = StudentAttendance.objects.create_attendance(class_name, student_id, period)
            std_attendance.status = attendance_status
            std_attendance.save()
            return redirect('attendance:attendance-list')
    else:
        form = AttendanceForm()

    context = {
        'form': form,
        'student': student
    }
    return render(request, 'attendance/mark_student_attendance.html', context)

@login_required
def mark_employee_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            period = form.cleaned_data['period']
            attendance_status = form.cleaned_data['status']
            emp_attendance = EmployeeAttendance.objects.create(
                employee=request.user,
                period=period,
                status=attendance_status
            )
            emp_attendance.save()
            return redirect('attendance:attendance-list')
    else:
        form = AttendanceForm()

    context = {
        'form': form
    }
    return render(request, 'attendance/mark_employee_attendance.html', context)

@login_required
def approve_employee_attendance(request, attendance_id):
    attendance = get_object_or_404(EmployeeAttendance, id=attendance_id)
    if request.user == attendance.employee.chief_executive:
        attendance.is_approved = True
        attendance.save()
    return redirect('attendance:attendance-list')

@login_required
def attendance_list(request):
    search_form = AttendanceSearchForm(request.GET)

    student_attendance = StudentAttendance.objects.filter(student__class_name__teacher=request.user)
    employee_attendance = EmployeeAttendance.objects.filter(employee__chief_executive=request.user)

    if search_form.is_valid():
        date = search_form.cleaned_data.get('date')
        student_name = search_form.cleaned_data.get('student_name')
        student_id = search_form.cleaned_data.get('student_id')
        class_name = search_form.cleaned_data.get('class_name')
        employee_name = search_form.cleaned_data.get('employee_name')
        employee_id = search_form.cleaned_data.get('employee_id')

        # Perform filtering based on the search criteria
        if date:
            student_attendance = student_attendance.filter(date=date)
            employee_attendance = employee_attendance.filter(date=date)
        
        if student_name:
            student_attendance = student_attendance.filter(student__name__icontains=student_name)
        
        if student_id:
            student_attendance = student_attendance.filter(student__id=student_id)
        
        if class_name:
            student_attendance = student_attendance.filter(class_name__name__icontains=class_name)
        
        if employee_name:
            employee_attendance = employee_attendance.filter(employee__name__icontains=employee_name)
        
        if employee_id:
            employee_attendance = employee_attendance.filter(employee__id=employee_id)

        # Add additional filters as needed

    context = {
        'student_attendance': student_attendance,
        'employee_attendance': employee_attendance,
        'search_form': search_form,
    }
    return render(request, 'attendance/attendance_list.html', context)

def attendance_report(request):
    # Construct the attendance report programmatically
    student_attendance = StudentAttendance.objects.all()
    employee_attendance = EmployeeAttendance.objects.all()

    # Generate the report content
    report_content = render_to_string('attendance/attendance_report.html', {
        'student_attendance': student_attendance,
        'employee_attendance': employee_attendance,
    })

    # Create the HTTP response with the report content
    response = HttpResponse(report_content, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="attendance_report.pdf"'

    return response

@login_required
def bulk_mark_student_attendance(request, class_name):
    if request.method == 'POST':
        form = BulkAttendanceForm(request.POST)
        if form.is_valid():
            status = form.cleaned_data['status']
            students = EnrolledStudent.objects.filter(class_name__name=class_name)
            for student in students:
                std_attendance = StudentAttendance.objects.create_attendance(class_name, student.id, period=None)
                std_attendance.status = status
                std_attendance.save()
            return redirect('attendance:attendance-list')
    else:
        form = BulkAttendanceForm()

    context = {
        'form': form,
        'class_name': class_name
    }
    return render(request, 'attendance/bulk_mark_student_attendance.html', context)
