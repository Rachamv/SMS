from django import forms
from django.core.exceptions import ValidationError

from .models import LeaveRequest, EducationInfo, TrainingInfo, EmployeeJobInfo, ExperienceInfo, PersonalInfo, EmployeeDocument


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = [
            'name',
            'photo',
            'date_of_birth',
            'place_of_birth',
            'nationality',
            'religion',
            'gender',
            'blood_group',
            'e_tin',
            'nid',
            'driving_license_passport',
            'phone_no',
            'email',
            'father_name',
            'mother_name',
            'marital_status',
            'address',
            'emergency_contact',
        ]


class EmployeeReportForm(forms.Form):
    employee_id = forms.IntegerField(label='Employee ID')

    def clean_employee_id(self):
        employee_id = self.cleaned_data['employee_id']
        if not PersonalInfo.objects.filter(id=employee_id).exists():
            raise ValidationError('Invalid employee ID')
        return employee_id


class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        exclude = ('status',)


class EmployeeDocumentForm(forms.ModelForm):
    class Meta:
        model = EmployeeDocument
        fields = ('document',)
