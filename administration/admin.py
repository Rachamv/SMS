from django.contrib import admin
from .models import ChiefExecutive, HeadTeacher, Secretary

@admin.register(ChiefExecutive)
class ChiefExecutiveAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')

@admin.register(HeadTeacher)
class HeadTeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')

@admin.register(Secretary)
class SecretaryAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
