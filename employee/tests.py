from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import LeaveRequest, EmployeeInfo, EmployeeJobInfo
from attendance.models import EmployeeAttendance
from io import BytesIO
from reportlab.pdfgen import canvas


class EmployeeAppTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')

    def test_leave_request(self):
        # Create a leave request
        response = self.client.post(reverse('employee:leave_request'), {
            'start_date': '2023-01-01',
            'end_date': '2023-01-05',
            'reason': 'Vacation',
        })
        self.assertEqual(response.status_code, 302)  # Check if redirecting

        # Check if the leave request is created
        leave_request = LeaveRequest.objects.last()
        self.assertEqual(leave_request.start_date.strftime('%Y-%m-%d'), '2023-01-01')
        self.assertEqual(leave_request.end_date.strftime('%Y-%m-%d'), '2023-01-05')
        self.assertEqual(leave_request.reason, 'Vacation')
        self.assertEqual(leave_request.status, 'pending')

    def test_employee_report(self):
        # Create an employee
        employee = EmployeeInfo.objects.create(name='John Doe')

        # Create an employee job info
        job_info = EmployeeJobInfo.objects.create(
            personal_info=employee,
            designation='Engineer',
            department='IT'
        )

        # Create an employee attendance record
        attendance = EmployeeAttendance.objects.create(
            employee=job_info,
            date='2023-01-01',
            status='present'
        )

        # Generate employee report
        response = self.client.post(reverse('employee:employee_report'), {
            'employee_id': employee.id,
        })
        self.assertEqual(response.status_code, 200)  # Check if successful

        # Get the PDF content from the response
        pdf_data = response.content

        # Load the PDF content into a BytesIO buffer
        buffer = BytesIO(pdf_data)

        # Create a PDF canvas from the buffer
        pdf = canvas.Canvas(buffer)

        # Extract text from the PDF
        pdf_text = pdf.extractText()

        # Check if the employee name is present in the PDF
        self.assertIn('John Doe', pdf_text)

        # Check if the designation is present in the PDF
        self.assertIn('Designation: Engineer', pdf_text)

        # Check if the department is present in the PDF
        self.assertIn('Department: IT', pdf_text)

        # Close the PDF canvas
        pdf.showPage()
        pdf.save()

        # Close the BytesIO buffer
        buffer.close()

    def test_employee_report_download(self):
        # Create an employee and other necessary objects
        employee = EmployeeInfo.objects.create(name='John Doe')
        job_info = EmployeeJobInfo.objects.create(
            Employee_info=employee,
            designation='Engineer',
            department='IT'
        )
        attendance = EmployeeAttendance.objects.create(
            employee=job_info,
            date='2023-01-01',
            status='present'
        )

        response = self.client.post(reverse('employee:employee_report'), {
            'employee_id': employee.id,
        })
        self.assertEqual(response.status_code, 200)  # Check if successful

        # Check if the content type of the response is correct
        self.assertEqual(response['Content-Type'], 'application/pdf')

        # Check if the file is downloaded with the correct filename
        self.assertEqual(
            response['Content-Disposition'],
            'attachment; filename="employee_report.pdf"'
        )

        # Check if the file size is not zero
        self.assertTrue(len(response.content) > 0)
