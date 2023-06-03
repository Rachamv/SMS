from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Teacher, TeachingAssignment, SpecialReport, Attendance, Test, Exam, TestResult, ExamResult, LessonPlan
from .forms import LessonPlanForm, TeachingAssignmentForm, SpecialReportForm, AttendanceForm, TestForm, ExamForm, TestResultForm, ExamResultForm


class TeacherModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.teacher = Teacher.objects.create(user=self.user, name='John Doe')

    def test_teacher_name(self):
        self.assertEqual(self.teacher.name, 'John Doe')


class SpecialReportCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.teacher = Teacher.objects.create(user=self.user, name='John Doe')

    def test_special_report_create_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('teacher:special_report_create', kwargs={'teacher_id': self.teacher.id}))
        self.assertEqual(response.status_code, 200)


class AttendanceCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.teacher = Teacher.objects.create(user=self.user, name='John Doe')

    def test_attendance_create_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('teacher:attendance_create', kwargs={'teacher_id': self.teacher.id, 'class_id': 1}))
        self.assertEqual(response.status_code, 200)


class TestCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.teacher = Teacher.objects.create(user=self.user, name='John Doe')

    def test_test_create_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('teacher:test_create', kwargs={'teacher_id': self.teacher.id}))
        self.assertEqual(response.status_code, 200)


class ExamCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.teacher = Teacher.objects.create(user=self.user, name='John Doe')

    def test_exam_create_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('teacher:exam_create', kwargs={'teacher_id': self.teacher.id}))
        self.assertEqual(response.status_code, 200)


class TestResultCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.teacher = Teacher.objects.create(user=self.user, name='John Doe')
        self.test = Test.objects.create(teacher=self.teacher, subject='Math', class_instance='Class 1', date='2023-01-01', max_marks=100, passing_marks=50)

    def test_test_result_create_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('teacher:test_result_create', kwargs={'test_id': self.test.id, 'student_id': 1}))
        self.assertEqual(response.status_code, 200)


class ExamResultCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.teacher = Teacher.objects.create(user=self.user, name='John Doe')
        self.exam = Exam.objects.create(teacher=self.teacher, subject='Science', class_instance='Class 1', date='2023-01-01', max_marks=100, passing_marks=50)

    def test_exam_result_create_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('teacher:exam_result_create', kwargs={'exam_id': self.exam.id, 'student_id': 1}))
        self.assertEqual(response.status_code, 200)

class LessonPlanCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_lesson_plan_create_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('lesson_plan_create'))
        self.assertEqual(response.status_code, 200)

    def test_lesson_plan_create_view_post(self):
        self.client.login(username='testuser', password='testpassword')
        form_data = {
            'title': 'Test Lesson Plan',
            'description': 'This is a test lesson plan.',
        }
        response = self.client.post(reverse('lesson_plan_create'), form_data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission
        self.assertEqual(LessonPlan.objects.count(), 1)
        self.assertEqual(LessonPlan.objects.first().title, 'Test Lesson Plan')


class LessonPlanUpdateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.lesson_plan = LessonPlan.objects.create(title='Original Title', description='Original Description')

    def test_lesson_plan_update_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('lesson_plan_update', kwargs={'lessonplan_id': self.lesson_plan.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Original Title')  # Check if original data is displayed in the form

    def test_lesson_plan_update_view_post(self):
        self.client.login(username='testuser', password='testpassword')
        form_data = {
            'title': 'Updated Title',
            'description': 'Updated Description',
        }
        response = self.client.post(reverse('lesson_plan_update', kwargs={'lessonplan_id': self.lesson_plan.id}), form_data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission
        self.lesson_plan.refresh_from_db()
        self.assertEqual(self.lesson_plan.title, 'Updated Title')
        self.assertEqual(self.lesson_plan.description, 'Updated Description')


class LessonPlanDeleteViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.lesson_plan = LessonPlan.objects.create(title='Test Lesson Plan', description='Test Description')

    def test_lesson_plan_delete_view_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('lesson_plan_delete', kwargs={'lessonplan_id': self.lesson_plan.id}))
        self.assertEqual(response.status_code, 302)  # Redirect after successful deletion
        self.assertFalse(LessonPlan.objects.filter(id=self.lesson_plan.id).exists())


class LessonPlanDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.lesson_plan = LessonPlan.objects.create(title='Test Lesson Plan', description='Test Description')

    def test_lesson_plan_detail_view(self):
        response = self.client.get(reverse('lesson_plan_detail', kwargs={'lessonplan_id': self.lesson_plan.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Lesson Plan')


class LessonPlanListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        LessonPlan.objects.create(title='Lesson Plan 1', description='Description 1')
        LessonPlan.objects.create(title='Lesson Plan 2', description='Description 2')

    def test_lesson_plan_list_view(self):
        response = self.client.get(reverse('lesson_plan_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Lesson Plan 1')
        self.assertContains(response, 'Lesson Plan 2')

