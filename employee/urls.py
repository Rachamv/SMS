from django.urls import path
from . import views

app_name = 'employee'

urlpatterns = [
    path('detail/<int:employee_id>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('leave-request/', views.leave_request, name='leave_request'),
    path('report/', views.employee_report, name='employee_report'),
    path('upload-document/', views.upload_document, name='upload_document'),
    path('document-list/', views.document_list, name='document_list'),
]
