from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .forms import EditProfileForm
from vehicles.models import Booking, Testimonial
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')


@login_required
def my_bookings(request):
    my_bookings = Booking.objects.filter(user=request.user)    
    context = {
        'my_bookings': my_bookings
    }
    return render(request, 'users/my_bookings.html', context)


@login_required
def my_testimonies(request):
    my_testimonials = Testimonial.objects.filter(user=request.user)
    context = {
        'my_testimonials': my_testimonials
    }
    return render(request, 'users/my_testimonies.html', context)    

@login_required
def edit_profile(request):
    if request.method == 'POST':
        edit_profile_form = EditProfileForm(request.POST or None, request.FILES, instance=request.user)
        if edit_profile_form.is_valid():
            edit_profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('users:dashboard')
    else:
        edit_profile_form = EditProfileForm(instance=request.user)
    context = {
        'edit_profile_form': edit_profile_form
    }

    return render(request, 'users/edit_profile.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('users:dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form': form
    }
    return render(request, 'users/change_password.html', context)


@login_required
def user_logout(request):
    # Logout user
    logout(request)
    # Return success message
    messages.info(request, 'See you soon 🙂')
    # Redirect to home page
    return redirect(request.META.get('HTTP_REFERER'))
