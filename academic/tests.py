from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Department, ClassInfo, Section, Session, GuideTeacher, ClassRegistration


class AcademicAppTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_department_list_view(self):
        url = reverse('add-department')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'academic/add-department.html')

    def test_grade_list_view(self):
        url = reverse('add-grade')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'academic/add-grade.html')

    def test_class_list_view(self):
        url = reverse('create-class')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'academic/create-class.html')

    def test_section_list_view(self):
        url = reverse('create-section')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'academic/create-section.html')

    def test_session_list_view(self):
        url = reverse('create-session')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'academic/create-session.html')

    def test_class_registration_view(self):
        url = reverse('class-registration')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'academic/class-registration.html')

    def test_class_list_view(self):
        url = reverse('class-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'academic/class-list.html')

    def test_guide_teacher_list_view(self):
        url = reverse('guide-teacher')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'academic/create-guide-teacher.html')

    def test_create_department(self):
        department_count = Department.objects.count()
        url = reverse('add-department')
        data = {'name': 'Mathematics'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Department.objects.count(), department_count + 1)
        self.assertTrue(Department.objects.filter(name='Mathematics').exists())

    # Add more test cases for other views and models as needed

