from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    path('student/<int:class_name>/<int:student_id>/', views.mark_student_attendance, name='mark-student-attendance'),
    path('student/bulk/', views.bulk_mark_student_attendance, name='bulk-mark-student-attendance'),  # Add the URL for bulk marking of student attendance
    path('employee/', views.mark_employee_attendance, name='mark-employee-attendance'),
    path('employee/approve/<int:attendance_id>/', views.approve_employee_attendance, name='approve-employee-attendance'),
    path('', views.attendance_list, name='attendance-list'),
    path('attendance/search/', views.attendance_search, name='attendance-search'),
    path('attendance_report/', views.attendance_report, name='attendance-report'),
]
