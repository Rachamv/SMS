from django.contrib import admin
from .models import StudentAttendance, EmployeeAttendance, Period

@admin.register(StudentAttendance)
class StudentAttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'class_name', 'status', 'period', 'date')
    list_filter = ('class_name', 'status', 'period', 'date')
    search_fields = ('student__student__personal_info__name',)
    date_hierarchy = 'date'

@admin.register(EmployeeAttendance)
class EmployeeAttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'status', 'date')
    list_filter = ('status', 'date')
    search_fields = ('employee__name',)
    date_hierarchy = 'date'

@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time')