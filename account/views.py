from django.shortcuts import render
from .models import UserProfile, UserRegistration

def user_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {'user_profile': user_profile}
    return render(request, 'user_profile.html', context)

def user_registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        date_of_birth = request.POST['date_of_birth']
        role = request.POST['role']
        
        # Create UserRegistration object
        user_registration = UserRegistration.objects.create(
            user=request.user,
            name=name,
            email=email,
            date_of_birth=date_of_birth,
            role=role
        )
        
        # Create UserProfile object
        user_profile = UserProfile.objects.create(
            user=request.user,
            name=name,
            photo='photos/default.jpg',
            gender='',
            employee_type=role,
            admin=None,
            director=None,
            register=None,
            teacher=None,
            parent=None,
            student=None,
            registration=user_registration
        )
        
        return render(request, 'registration_success.html')
    
    return render(request, 'user_registration.html')


def user_upDate(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_update')
    else:
        form = UserProfileForm(instance=user_user_update)

    context = {'user_update': user_profile, 'form': form}
    return render(request, 'user_update.html', context)

