from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password1']
        confirm_password = request.POST['password2']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username,
                        first_name=firstname,
                        last_name=lastname,
                        email=email,
                        password=password
                    )
                    auth.login(request, user)
                    if not user.is_staff:
                        messages.success(
                            request, 'Account created successfully, please complete your profile'
                        )
                        return redirect('users:edit_profile')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    return render(request, 'accounts/register.html')


# Login View for Users
def user_login(request):

    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('home')
    else:
        # Check when form is submitted
        if request.method == 'POST':
            # Get form data
            email = request.POST['email']
            password = request.POST['password']

            # Check if user's email exitss in the database
            if User.objects.all().filter(email=email).exists():
                # Get username of user based on email from database (Because django cannot authenticate with email, it must be username)
                username = User.objects.get(email=email).username
                # Authenticate user
                user = authenticate(username=username, password=password)

                # Check if user is authenticated
                if user:
                    # Check if user is active
                    if user.is_active:
                        # If user is active, login user
                        login(request, user)
                        # Return success message
                        messages.success(request, 'Welcome back')
                        # Redirect to home page
                        if user.is_staff:
                            return redirect('admin_panel:dashboard')
                        else:
                            return redirect('users:dashboard')

                    # If user is not active, return error message
                    else:
                        # Return error message
                        messages.warning(request, 'Account is not active')
                        # return user to home page
                        return redirect('home')

                # If user is not authenticated, return error message
                else:
                    # Return error message
                    messages.error(request, 'Incorrect email or password')
                    # Renders login page back to user
                    return render(request, 'accounts/login.html')

            # If user's email does not exist in the database, return error message
            else:
                # Return error message
                messages.error(request, 'Please enter valid email')
                # Renders login page back to user
                return render(request, 'accounts/login.html')

        # If form is not submitted, render login page
        return render(request, 'accounts/login.html')


# Logout View for Users
# @login_required makes sure a user is logged in before accessing a page
@login_required
def user_logout(request):
    # Logout user
    logout(request)
    # Return success message
    messages.info(request, 'See you soon 🙂')
    # Redirect to home page
    return redirect(request.META.get('HTTP_REFERER'))
