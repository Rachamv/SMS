from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_images')

    # Recurrence fields
    is_recurring = models.BooleanField(default=False)
    recurrence_type = models.CharField(max_length=20, blank=True, null=True)
    recurrence_frequency = models.PositiveIntegerField(blank=True, null=True)
    recurrence_interval = models.PositiveIntegerField(blank=True, null=True)
    recurrence_end_date = models.DateTimeField(blank=True, null=True)

    # Attendance field
    students_attending = models.ManyToManyField('student.Student', blank=True)
    parents_attending = models.ManyToManyField('parents.Parent', blank=True)
    teachers_attending = models.ManyToManyField('teacher.Teacher', blank=True)

    # Visibility field
    visibility_choices = (
        ('public', 'Public'),
        ('internal', 'Internal'),
        ('restricted', 'Restricted'),
    )
    visibility = models.CharField(max_length=20, choices=visibility_choices, default='public')

    # Sponsorship field
    sponsors = models.ManyToManyField('Sponsor', blank=True)

    

class EventDocument(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    document = models.FileField(upload_to='event_documents')

    

class EventFeedback(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0)
    comment = models.TextField(blank=True)

    

class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    show_sponsor = models.BooleanField(default=True)
    
    
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'location', 'organizer')
    list_filter = ('start_date', 'end_date', 'organizer')
    search_fields = ('title', 'description')
    