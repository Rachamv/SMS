from django.urls import path

from . import views

urlpatterns = [
    path('add-department', views.add_department, name='add-department'),
    path('add-grade', views.add_grade, name='add-grade'),
    path('create-class', views.add_class, name='create-class'),
    path('create-section', views.create_section, name='create-section'),
    path('create-session', views.create_session, name='create-session'),
    path('class-registration', views.class_registration, name='class-registration'),
    path('class-list', views.class_list, name='class-list'),
    path('guide-teacher', views.create_guide_teacher, name='guide-teacher'),
]
