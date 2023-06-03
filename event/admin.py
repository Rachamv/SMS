from django.contrib import admin
from .models import Event, EventDocument, EventFeedback, Sponsor

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'location', 'organizer')
    list_filter = ('start_date', 'end_date', 'organizer')
    search_fields = ('title', 'description')

@admin.register(EventDocument)
class EventDocumentAdmin(admin.ModelAdmin):
    pass

@admin.register(EventFeedback)
class EventFeedbackAdmin(admin.ModelAdmin):
    pass

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_sponsor')
    list_filter = ('show_sponsor',)
