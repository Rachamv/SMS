from django import forms
from academic.models import Subject, Grade
from student.models import Student
from .models import ExamResult, Test, StudentAttendance, SpecialReport, LessonPlan, Exam, TestResult


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['teacher', 'subject', 'class_instance', 'date', 'max_marks', 'passing_marks']
        widgets = {
            'teacher': forms.HiddenInput(),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'class_instance': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'max_marks': forms.NumberInput(attrs={'class': 'form-control'}),
            'passing_marks': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ExamResultForm(forms.ModelForm):
    class Meta:
        model = ExamResult
        fields = ['exam', 'student', 'marks_obtained', 'grade']
        widgets = {
            'exam': forms.Select(attrs={'class': 'form-control'}),
            'student': forms.Select(attrs={'class': 'form-control'}),
            'marks_obtained': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['exam'].queryset = Exam.objects.all()
        self.fields['student'].queryset = Student.objects.all()


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['teacher', 'subject', 'class_instance', 'date', 'max_marks', 'passing_marks']
        widgets = {
            'teacher': forms.HiddenInput(),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'class_instance': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'max_marks': forms.NumberInput(attrs={'class': 'form-control'}),
            'passing_marks': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subject'].queryset = Subject.objects.all()
        self.fields['class_instance'].queryset = Grade.objects.all()


class TestResultForm(forms.ModelForm):
    class Meta:
        model = TestResult
        fields = ['test', 'student', 'marks_obtained', 'grade']


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = StudentAttendance
        fields = ['class_instance', 'date', 'status', 'remarks']
        widgets = {
            'class_instance': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'remarks': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['class_instance'].queryset = Grade.objects.all()


class SpecialReportForm(forms.ModelForm):
    class Meta:
        model = SpecialReport
        fields = ['student', 'report']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'report': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].queryset = Student.objects.all()


class LessonPlanForm(forms.ModelForm):
    class Meta:
        model = LessonPlan
        fields = ['teacher', 'subject', 'class_instance', 'date', 'title', 'description']
        widgets = {
            'teacher': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'class_instance': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
