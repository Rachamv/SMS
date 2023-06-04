from django.contrib import admin
from .models import ChiefExecutive, Director, Secretary

@admin.register(ChiefExecutive)
class ChiefExecutiveAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')

@admin.register(Secretary)
class SecretaryAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
