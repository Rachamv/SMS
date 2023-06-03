from django.urls import path
from .views import (
    TeacherDetailView,
    SpecialReportCreateView,
    AttendanceCreateView,
    TestCreateView,
    ExamCreateView,
    TestResultCreateView,
    ExamResultCreateView,
    mark_attendance,
    give_special_report,
)

app_name = 'teacher'

urlpatterns = [
    path('<int:teacher_id>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('<int:teacher_id>/special-report/<int:student_id>/create/', SpecialReportCreateView.as_view(), name='special_report_create'),
    path('<int:teacher_id>/attendance/<int:class_id>/create/', AttendanceCreateView.as_view(), name='attendance_create'),
    path('<int:teacher_id>/test/create/', TestCreateView.as_view(), name='test_create'),
    path('<int:teacher_id>/exam/create/', ExamCreateView.as_view(), name='exam_create'),
    path('test-result/<int:test_id>/<int:student_id>/create/', TestResultCreateView.as_view(), name='test_result_create'),
    path('exam/create/', ExamCreateView.as_view(), name='exam_create'),
    path('exam/update/<int:exam_id>/', ExamUpdateView.as_view(), name='exam_update'),
    path('exam/delete/<int:exam_id>/', ExamDeleteView.as_view(), name='exam_delete'),
    path('exam/detail/<int:exam_id>/', ExamDetailView.as_view(), name='exam_detail'),
    path('exam-result/<int:exam_id>/<int:student_id>/create/', ExamResultCreateView.as_view(), name='exam_result_create'),
    path('mark-attendance/<int:class_instance_id>/', mark_attendance, name='mark_attendance'),
    path('give-special-report/<int:student_id>/', give_special_report, name='give_special_report'),
    path('<int:teacher_id>/lesson-plan/create/', LessonPlanCreateView.as_view(), name='lesson_plan_create'),
    path('<int:teacher_id>/lesson-plan/<int:lesson_plan_id>/', LessonPlanDetailView.as_view(), name='lesson_plan_detail'),
    path('<int:teacher_id>/lesson-plan/<int:lesson_plan_id>/update/', LessonPlanUpdateView.as_view(), name='lesson_plan_update'),
    path('<int:teacher_id>/lesson-plan/<int:lesson_plan_id>/delete/', LessonPlanDeleteView.as_view(), name='lesson_plan_delete'),
]
