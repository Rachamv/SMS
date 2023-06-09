from django.contrib import admin

from . import models


admin.site.register(models.Department)
admin.site.register(models.Grade)
admin.site.register(models.ClassInfo)
admin.site.register(models.Section)
admin.site.register(models.Session)
admin.site.register(models.GuideTeacher)
admin.site.register(models.ClassRegistration)


@admin.register(models.ClassInfo)
class ClassInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_name')
