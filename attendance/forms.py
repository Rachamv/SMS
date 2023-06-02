from django import forms
from .models import StudentAttendance, EmployeeAttendance

class StudentAttendanceForm(forms.ModelForm):
    class Meta:
        model = StudentAttendance
        fields = ['status', 'period']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'period': forms.Select(attrs={'class': 'form-control'}),
        }

class EmployeeAttendanceForm(forms.ModelForm):
    class Meta:
        model = EmployeeAttendance
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class AttendanceSearchForm(forms.Form):
    date = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date'}))
    student_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Student Name'}))
    student_id = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Student ID'}))
    class_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Class Name'}))
    employee_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Employee Name'}))
    employee_id = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Employee ID'}))
    # Add additional search fields as needed

    def clean(self):
        cleaned_data = super().clean()
        # Perform additional validation or cleaning if necessary
        return cleaned_data

class BulkAttendanceForm(forms.Form):
    status = forms.ChoiceField(choices=(('P', 'Present'), ('A', 'Absent')), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
