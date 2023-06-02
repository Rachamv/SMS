from django.shortcuts import render, redirect
from .forms import AddressForm, EmergencyContactForm
from .models import Address, EmergencyContact
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def address(request):
    try:
        address = Address.objects.get(user=request.user)
    except Address.DoesNotExist:
        address = None

    try:
        emergency_contact = EmergencyContact.objects.get(address=address)
    except EmergencyContact.DoesNotExist:
        emergency_contact = None

    context = {
        'address': address,
        'emergency_contact': emergency_contact
    }
    return render(request, 'address/address.html', context)


@login_required(login_url='login')
def update_address(request):
    try:
        address = Address.objects.get(user=request.user)
    except Address.DoesNotExist:
        address = None

    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('address')
    else:
        form = AddressForm(instance=address)

    context = {
        'form': form
    }
    return render(request, 'address/update_address.html', context)


@login_required(login_url='login')
def update_emergency_contact(request):
    try:
        address = Address.objects.get(user=request.user)
    except Address.DoesNotExist:
        address = None

    try:
        emergency_contact = EmergencyContact.objects.get(address=address)
    except EmergencyContact.DoesNotExist:
        emergency_contact = None

    if request.method == 'POST':
        form = EmergencyContactForm(request.POST, instance=emergency_contact)
        if form.is_valid():
            emergency_contact = form.save(commit=False)
            emergency_contact.address = address
            emergency_contact.save()
            return redirect('address')
    else:
        form = EmergencyContactForm(instance=emergency_contact)

    context = {
        'form': form
    }
    return render(request, 'address/update_emergency_contact.html', context)
