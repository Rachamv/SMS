from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from student.models import EnrolledStudent
from .models import StudentAttendance, EmployeeAttendance, Period

class AttendanceTestCase(TestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a student and class for testing
        self.class_name = Class.objects.create(name='Test Class')
        self.student = EnrolledStudent.objects.create(name='Test Student', class_name=self.class_name)

        # Create an employee for testing
        self.employee = Employee.objects.create(name='Test Employee')

        # Create a period for testing
        self.period = Period.objects.create(name='Test Period')

    def test_mark_student_attendance(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Send a POST request to mark the student's attendance
        url = reverse('attendance:mark-student-attendance', args=[self.class_name.id, self.student.id])
        response = self.client.post(url, {'status': 'present', 'period': self.period.id})

        # Check if the response is successful
        self.assertEqual(response.status_code, 302)

        # Check if the student attendance record is created
        attendance = StudentAttendance.objects.get(student=self.student, class_name=self.class_name)
        self.assertEqual(attendance.status, 'present')
        self.assertEqual(attendance.period, self.period)

    def test_mark_employee_attendance(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Send a POST request to mark the employee's attendance
        url = reverse('attendance:mark-employee-attendance')
        response = self.client.post(url, {'status': 'present', 'period': self.period.id})

        # Check if the response is successful
        self.assertEqual(response.status_code, 302)

        # Check if the employee attendance record is created
        attendance = EmployeeAttendance.objects.get(employee=self.employee)
        self.assertEqual(attendance.status, 'present')
        self.assertEqual(attendance.period, self.period)

    def test_attendance_list(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Send a GET request to the attendance list view
        url = reverse('attendance:attendance-list')
        response = self.client.get(url)

        # Check if the response is successful
        self.assertEqual(response.status_code, 200)

        # Check if the student and employee attendance records are included in the context
        self.assertIn('student_attendance', response.context)
        self.assertIn('employee_attendance', response.context)

    def test_attendance_report(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Send a GET request to the attendance report view
        url = reverse('attendance:attendance-report')
        response = self.client.get(url)

        # Check if the response is successful
        self.assertEqual(response.status_code, 200)

        # Check if the response content type is PDF
        self.assertEqual(response['Content-Type'], 'application/pdf')

    def test_bulk_mark_student_attendance(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Send a POST request to mark attendance for all students in a class
        url = reverse('attendance:bulk-mark-student-attendance', args=[self.class_name.id])
        response = self.client.post(url, {'status': 'present'})

        # Check if the response is successful
        self.assertEqual(response.status_code, 302)

        # Check if attendance records are created for all students in the class
        students = EnrolledStudent.objects.filter(class_name=self.class_name)
        for student in students:
            attendance = StudentAttendance.objects.get(student=student, class_name=self.class_name)
            self.assertEqual(attendance.status, 'present')

