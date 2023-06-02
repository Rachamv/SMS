from django.contrib import admin
from .models import (
    LeaveRequest,
    EducationInfo,
    TrainingInfo,
    EmployeeJobInfo,
    ExperienceInfo,
    PersonalInfo,
    EmployeeDocument,
)


@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'start_date', 'end_date', 'status')
    list_filter = ('status', 'employee__name')
    search_fields = ('employee__name', 'reason')


@admin.register(EducationInfo)
class EducationInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'personal_info', 'degree', 'institution', 'year')


@admin.register(TrainingInfo)
class TrainingInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'personal_info', 'training', 'institution', 'year')


@admin.register(EmployeeJobInfo)
class EmployeeJobInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'personal_info', 'designation', 'department')
    list_filter = ('department',)
    search_fields = ('personal_info__name', 'designation')


@admin.register(ExperienceInfo)
class ExperienceInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'personal_info', 'organization', 'position', 'start_date', 'end_date')


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_of_birth', 'gender', 'blood_group')
    search_fields = ('name', 'email')


@admin.register(EmployeeDocument)
class EmployeeDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'document', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('employee__name', 'document')




