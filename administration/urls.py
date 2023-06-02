from django.urls import path
from . import views

app_name = 'administration'

urlpatterns = [
    path('login/', views.admin_login, name='login'),
    path('logout/', views.admin_logout, name='logout'),
    path('chief-executive/add/', views.add_chief_executive, name='add_chief_executive'),
    path('chief-executive/list/', views.chief_executive_list, name='chief_executive_list'),
    path('head-teacher/list/', views.head_teacher_list, name='head_teacher_list'),
    path('secretary/list/', views.secretary_list, name='secretary_list'),
]
