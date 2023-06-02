from django.test import TestCase
from django.contrib.auth.models import User
from .models import ChiefExecutive, HeadTeacher, Secretary

class ChiefExecutiveTestCase(TestCase):
    def setUp(self):
        self.chief_executive = ChiefExecutive.objects.create(name='John Doe')

    def test_str_representation(self):
        self.assertEqual(str(self.chief_executive), 'John Doe')

    def test_grant_manage_everything_permission(self):
        self.chief_executive.grant_manage_everything_permission()
        self.assertTrue(self.chief_executive.has_perm('administration.can_manage_everything'))

class HeadTeacherTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='teacher', password='password')
        self.head_teacher = HeadTeacher.objects.create(user=self.user, name='Jane Smith')

    def test_str_representation(self):
        self.assertEqual(str(self.head_teacher), 'Jane Smith')

    def test_teachers_field(self):
        self.assertEqual(self.head_teacher.teachers.count(), 0)

class SecretaryTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='secretary', password='password')
        self.secretary = Secretary.objects.create(user=self.user, name='Alice Brown')

    def test_str_representation(self):
        self.assertEqual(str(self.secretary), 'Alice Brown')

    def test_can_delete_student_payments(self):
        self.assertFalse(self.secretary.has_perm('administration.delete_studentpayment'))
