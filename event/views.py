from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event
from .forms import EventForm


@login_required
def event_list(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'event/event_list.html', context)


@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    context = {'event': event}
    return render(request, 'event/event_detail.html', context)


@login_required
def create_event(request):
    if not request.user.groups.filter(name__in=['Director', 'ChiefExecutive']).exists():
        messages.error(request, 'You do not have permission to create an event.')
        return redirect('event_list')

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            form.save_m2m()
            messages.success(request, 'Event created successfully.')
            return redirect('event_list')
    else:
        form = EventForm()
    context = {'form': form}
    return render(request, 'event/create_event.html', context)


@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if event.organizer != request.user:
        messages.error(request, 'You do not have permission to edit this event.')
        return redirect('event_detail', event_id=event_id)

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            form.save_m2m()
            messages.success(request, 'Event updated successfully.')
            return redirect('event_detail', event_id=event_id)
    else:
        form = EventForm(instance=event)
    context = {'form': form, 'event': event}
    return render(request, 'event/edit_event.html', context)


@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if event.organizer != request.user:
        messages.error(request, 'You do not have permission to delete this event.')
        return redirect('event_detail', event_id=event_id)

    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully.')
        return redirect('event_list')

    context = {'event': event}
    return render(request, 'event/delete_event.html', context)
