from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import ChiefExecutive, Director, Secretary
from .forms import AdminLoginForm, ChiefExecutiveForm

def admin_login(request):
    forms = AdminLoginForm()
    if request.method == 'POST':
        forms = AdminLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    context = {'forms': forms}
    return render(request, 'administration/login.html', context)

def admin_logout(request):
    logout(request)
    return redirect('login')

def add_chief_executive(request):
    forms = ChiefExecutiveForm()
    if request.method == 'POST':
        forms = ChiefExecutiveForm(request.POST)
        if forms.is_valid():
            chief_executive = forms.save()
            chief_executive.grant_manage_everything_permission()
            return redirect('chief_executive_list')
    context = {'forms': forms}
    return render(request, 'administration/add_chief_executive.html', context)

def chief_executive_list(request):
    chief_executives = ChiefExecutive.objects.all()
    context = {'chief_executives': chief_executives}
    return render(request, 'administration/chief_executive_list.html', context)

def head_teacher_list(request):
    if request.user.is_authenticated and request.user.is_superuser:
        head_teachers = Director.objects.all()
    else:
        head_teachers = Director.objects.filter(user=request.user)
    context = {'head_teachers': head_teachers}
    return render(request, 'administration/head_teacher_list.html', context)

def secretary_list(request):
    if request.user.is_authenticated and request.user.is_superuser:
        secretaries = Secretary.objects.all()
    else:
        secretaries = Secretary.objects.filter(user=request.user)
    context = {'secretaries': secretaries}
    return render(request, 'administration/secretary_list.html', context)
