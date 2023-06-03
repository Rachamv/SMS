from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'description',
            'start_date',
            'end_date',
            'location',
            'image',
            'is_recurring',
            'recurrence_type',
            'recurrence_frequency',
            'recurrence_interval',
            'recurrence_end_date',
            'visibility',
            'sponsors',
        ]
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
        }