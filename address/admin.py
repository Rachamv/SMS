from django.contrib import admin
from .models import Address, EmergencyContact

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'street', 'city', 'state', 'postal_code', 'country')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'street', 'city', 'state', 'postal_code', 'country')

@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'contact_name', 'contact_relationship', 'contact_address')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'contact_name', 'contact_relationship')
