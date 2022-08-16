from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Vehicle
from .forms import TestimonialForm, BookingForm
from django.contrib import messages
from django.db.models import Q


# Create your views here.


def vehicles(request):
   vehicles = Vehicle.objects.all()
   p = Paginator(vehicles, 3)
   page = request.GET.get('page')
   paginated_vehicles = p.get_page(page)
   context = {
      'paginated_vehicles': paginated_vehicles,      
   }
   return render(request, 'vehicles/vehicles.html', context)



def vehicle_details(request, slug):
   vehicle = get_object_or_404(Vehicle, slug=slug)   
   
   if request.method == "POST":
      testimonial_form = TestimonialForm(request.POST)
      booking_form = BookingForm(request.POST)
      if testimonial_form.is_valid():
         instance = testimonial_form.save(commit=False)
         instance.user = request.user
         instance.vehicle = vehicle
         instance.save()
         messages.success(request, 'Testimony successful, thank you 🙂')
         return redirect('vehicle_details', slug=slug)

      if booking_form.is_valid():
         instance = booking_form.save(commit=False)
         instance.user = request.user
         instance.vehicle = vehicle
         instance.save()
         messages.success(request, f'Your have successfully booked {vehicle.vehicle_name}!')
         return redirect('vehicle_details', slug=slug)
   else:
      testimonial_form = TestimonialForm()
      booking_form = BookingForm()

   context = {      
      'testimonial_form': testimonial_form,
      'booking_form': booking_form,
      'vehicle': vehicle,
   }
   return render(request, 'vehicles/vehicle_details.html', context)


def search_vehicles(request):
   if request.method == "POST":
      search = request.POST['search']
      if search :         
         vehicles = Vehicle.objects.filter(
            Q(vehicle_name__icontains=search) | 
            Q(brand__name__icontains=search) |
            Q(year__icontains=search) |
            Q(color__icontains=search) |
            Q(fuel_type__icontains=search) |
            Q(price__icontains=search) |             
            Q(seats__icontains=search) |
            Q(transmission__icontains=search) |
            Q(drive__icontains=search) |
            Q(features__icontains=search) 
         ).order_by('vehicle_name')
         if vehicles:            
            return render(request, 'vehicles/search_vehicles.html', {'paginated_vehicles': vehicles})      
         else:
            return render(request, 'vehicles/search_vehicles.html')
      else:
         messages.error(request, 'Please enter a search term')
         return render(request, 'vehicles/search_vehicles.html')
   return render(request, 'vehicles/search_vehicles.html')

