from django.shortcuts import render, redirect
from .models import Inquiry, OurTeam, ContactUsDetails, Subscriber
from django.contrib import messages
from vehicles.models import Testimonial

# Home Page View
def home(request):
   active_testimonials = Testimonial.objects.filter(is_active=True)
   context = {
      'active_testimonials': active_testimonials
   }
   return render(request, 'fastcars/home.html', context)


# About Us View
def about(request):
   # Get all our team members from database
   team_members = OurTeam.objects.all()
   # Pass all info into a python dictionary
   context = {
      'team_members': team_members
   }
   # Pass the dictionary into the rendered page 
   return render(request, 'fastcars/about.html', context)



def services(request):
   return render(request, 'fastcars/services.html')

def contact(request):
   contact_us_details = ContactUsDetails.objects.first()
   if request.method == 'POST':
      inquirer = request.POST['name']
      email = request.POST['email']
      subject = request.POST['subject']
      message = request.POST['message']

      Inquiry.objects.create(name=inquirer, email=email, subject=subject, message=message)
      messages.success(request, 'Your inquiry has been sent!')
      

   context = {
      'contact_us_details': contact_us_details
   }

   return render(request, 'fastcars/contact.html', context)


def footer(request):
   if request.method == 'POST':      
      email = request.POST['email']      

      Subscriber.objects.create(email=email)
      
      messages.success(request, 'You have successfully subscribed to our newsletter!')
      return redirect(request.META.get('HTTP_REFERER'))   


def error_404(request, exception):
   return render(request, 'fastcars/error_404.html')