from django.contrib import admin
from .models import Teacher, TeachingAssignment, SpecialReport, Attendance, Test, Exam, TestResult, ExamResult, LessonPlan

admin.site.register(Teacher)
admin.site.register(TeachingAssignment)
admin.site.register(SpecialReport)
admin.site.register(Attendance)
admin.site.register(Test)
admin.site.register(Exam)
admin.site.register(TestResult)
admin.site.register(ExamResult)
admin.site.register(LessonPlan)
