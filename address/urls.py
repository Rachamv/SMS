from django.urls import path

from . import views

app_name = 'address'

urlpatterns = [
    path('update/', views.update_address, name='update-address'),
    path('emergency-contact/', views.update_emergency_contact, name='update-emergency-contact'),
]
