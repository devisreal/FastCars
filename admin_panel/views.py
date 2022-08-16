from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import User
from django.core.paginator import Paginator
from vehicles.models import Booking, Vehicle, Brand, Testimonial
from vehicles.forms import VehicleForm, UpdateTestimonialForm
from fastcars.models import Inquiry, OurTeam, ContactUsDetails, Subscriber
from fastcars.forms import Contact_Details_Form, Team_Members_Form
from django.contrib import messages

# ! Dashboard View for Admin Dashboard
# * @login_required makes sure a user is logged in before accessing this page
@login_required
def dashboard(request):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      total_users = len(User.objects.all().filter(is_staff=False))
      total_brands = len(Brand.objects.all())
      total_vehicles = len(Vehicle.objects.all())
      total_bookings = len(Booking.objects.all())
      total_testimonials = len(Testimonial.objects.all())
      total_inquiries = len(Inquiry.objects.all())      
      total_subscribers = len(Subscriber.objects.all())      

      context = {
         'total_users': total_users,
         'total_brands': total_brands,
         'total_vehicles': total_vehicles,
         'total_bookings': total_bookings,
         'total_testimonials': total_testimonials,
         'total_inquiries': total_inquiries,
         'total_subscribers': total_subscribers,
      }
      return render(request, 'admin_panel/dashboard.html', context)


# =========================================================== Vehicles ===========================================================
# View for all vehicles
@login_required
def vehicles(request):   
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      vehicles = Vehicle.objects.all()
      p = Paginator(vehicles, 2)
      page = request.GET.get('page')
      paginated_vehicles = p.get_page(page)

      context = {
         'paginated_vehicles': paginated_vehicles,
      }
      return render(request, 'admin_panel/vehicles/vehicles.html', context)


@login_required
def add_vehicle(request):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      if request.method == 'POST':
         add_vehicle_form = VehicleForm(request.POST, request.FILES)
         if add_vehicle_form.is_valid():
            add_vehicle_form.save()
            messages.success(request, 'Vehicle added successfully')
            return redirect('admin_panel:vehicles')
         else:
            messages.error(request, "An error occured")
            return redirect('admin_panel:vehicles')
      else:
         add_vehicle_form = VehicleForm()   
      context = {
         'add_vehicle_form': add_vehicle_form
      }
      return render(request, 'admin_panel/vehicles/add_vehicle.html', context)


@login_required
def edit_vehicle(request, slug):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      vehicle = get_object_or_404(Vehicle, slug=slug)
      if request.method == 'POST':
         add_vehicle_form = VehicleForm(
            request.POST or None, request.FILES, instance=vehicle)
         if add_vehicle_form.is_valid():
            add_vehicle_form.save()
            messages.success(request, 'Vehicle Updated successfully')
            return redirect('admin_panel:vehicles')
         else:
            messages.error(request, "An error occured")
            return redirect('admin_panel:vehicles')
      else:
         add_vehicle_form = VehicleForm(instance=vehicle)
      context = {
         'add_vehicle_form': add_vehicle_form,
         'vehicle': vehicle
      }
      return render(request, 'admin_panel/vehicles/edit_vehicle.html', context)

@login_required
def delete_vehicle(request, slug):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      vehicle = get_object_or_404(Vehicle, slug=slug)
      vehicle.delete()
      messages.success(request, 'Vehicle deleted successfully')
      return redirect('vehicles')
# =========================================================== Brands ===========================================================

# Brands View for Admin Dashboard
# @login_required makes sure a user is logged in before accessing this page
@login_required
def brands(request):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      brands = Brand.objects.all()

      if request.method == 'POST':
         name = request.POST['name']
         if name:
            brand = Brand(name=name)
            brand.save()
            messages.success(request, 'Brand created!')
            return redirect('admin_panel:brands')
         else:
            messages.error(request, 'Enter a brand !')
            return redirect('admin_panel:brands')

      context = {
         'brands': brands
      }
      return render(request, 'admin_panel/brands.html', context)

# Delete Subscriber Functionality for Admin Dashboard
# @login_required makes sure a user is logged in before accessing this page
@login_required
def delete_brand(request, id):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      brand = Brand.objects.get(id=id)
      brand.delete()
      messages.success(request, 'Brand successfully deleted!')
      return redirect('admin_panel:brands')


@login_required
def edit_brand(request, id):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      brand = Brand.objects.get(id=id)
      if request.method == 'POST':
         name = request.POST['name']
         if name:
            brand.name = name
            brand.save()
            messages.success(request, 'Brand successfully updated!')
            return redirect('admin_panel:brands')
      return redirect('admin_panel:brands')


# =========================================================== Users ===========================================================
@login_required
def users(request):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      users = User.objects.all()
      context = {
         'users': users
      }
      return render(request, 'admin_panel/users/users.html', context)


@login_required
def user_profile(request, slug):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      user = get_object_or_404(User, slug=slug)
      context = {
         'user': user
      }
      return render(request, 'admin_panel/users/user_profile.html', context)


@login_required
def delete_user(request, slug):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      user = User.objects.get(slug=slug)
      user.delete()
      messages.success(request, 'User successfully deleted!')
      return redirect('admin_panel:users')

# =========================================================== Bookings ===========================================================

@login_required
def bookings(request):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      bookings = Booking.objects.all().order_by('-id')
      context = {
         'bookings': bookings
      }
      return render(request, 'admin_panel/bookings/bookings.html', context)

@login_required
def confirm_booking(request, id):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      booking = Booking.objects.get(id=id)
      booking.is_active = True
      booking.save()
      messages.success(request, 'Booking confirmed')
      return redirect(request.META.get('HTTP_REFERER'))


@login_required
def cancel_booking(request, id):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      booking = Booking.objects.get(id=id)
      booking.is_active = False
      booking.save()
      messages.success(request, 'Booking cancelled')
      return redirect(request.META.get('HTTP_REFERER'))

@login_required
def vehicle_returned(request, id):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      booking = Booking.objects.get(id=id)
      booking.is_active = False
      booking.vehicle_returned = True
      booking.is_completed = True
      booking.save()
      messages.success(request, 'Vehicle returned')
      return redirect(request.META.get('HTTP_REFERER'))

# =========================================================== Testimonials ===========================================================
@login_required
def testimonials(request):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      testimonials = Testimonial.objects.all()
      context = {
         'testimonials': testimonials
      }
      return render(request, 'admin_panel/testimonials/testimonials.html', context)


@login_required
def testimonial_detail(request, id):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      testimonial = get_object_or_404(Testimonial, id=id)
      
      if request.method == "POST":
         update_testimonial_form = UpdateTestimonialForm(request.POST, request.FILES, instance=testimonial)
         if update_testimonial_form.is_valid():
            update_testimonial_form.save()
            messages.success(request, 'Testimonial updated!')
            return redirect('admin_panel:testimonials')
      else:
         update_testimonial_form = UpdateTestimonialForm(instance=testimonial)
      context = {
         'testimonial': testimonial,
         'update_testimonial_form': update_testimonial_form
      }
      return render(request, 'admin_panel/testimonials/testimonial_detail.html', context)

# =========================================================== Subscribers ===========================================================

# Subscribers View for Admin Dashboard
# @login_required makes sure a user is logged in before accessing this page
@login_required
def subscribers(request):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      subscribers = Subscriber.objects.all()
      context = {
         'subscribers': subscribers
      }
      return render(request, 'admin_panel/subscribers.html', context)

# Delete Subscriber Functionality for Admin Dashboard
# @login_required makes sure a user is logged in before accessing this page
@login_required
def delete_subscriber(request, id):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      subscriber = Subscriber.objects.get(id=id)
      subscriber.delete()
      messages.success(request, 'Subscriber deleted!')
      return redirect('admin_panel:subscribers')   


# =========================================================== Queries ===========================================================
@login_required
def queries(request):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      inquiries = Inquiry.objects.all()
      context = {
         'inquiries': inquiries
      }
      return render(request, 'admin_panel/query/queries.html', context)

@login_required
def query_detail(request, id):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      inquiry= get_object_or_404(Inquiry, id=id)
      context = {
         'inquiry': inquiry
      }
      return render(request, 'admin_panel/query/query_detail.html', context)

@login_required
def delete_query(request, id):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      query = Inquiry.objects.get(id=id)
      query.delete()
      messages.success(request, 'Query deleted!')
      return redirect('admin_panel:queries')


# =========================================================== Page Content ===========================================================
@login_required
def page_content(request):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      team_members = OurTeam.objects.all()
      contact_details = ContactUsDetails.objects.get(id=1)

      if request.method == "POST":      
         contact_form = Contact_Details_Form(request.POST or None, instance=contact_details)
         add_member_form = Team_Members_Form(request.POST, request.FILES)
         if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Contact details updated!')
            return redirect('admin_panel:page_content')
         if add_member_form.is_valid():
            add_member_form.save()
            messages.success(request, 'Added new member!')
            return redirect('admin_panel:page_content')
      else:      
         add_member_form = Team_Members_Form()
         contact_form = Contact_Details_Form(instance=contact_details)
         

      context = {
         'team_members': team_members,            
         'contact_details': contact_details,
         'contact_form': contact_form,
         'add_member_form': add_member_form

      }
      return render(request, 'admin_panel/page_content.html', context)


@login_required
def edit_member(request, id):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      member = OurTeam.objects.get(id=id)   
      if request.method == "POST":
         edit_member_form = Team_Members_Form(request.POST, request.FILES, instance=member)
         if edit_member_form.is_valid():
            edit_member_form.save()
            messages.success(request, 'Member updated!')
            return redirect('admin_panel:page_content')
      else:
         edit_member_form = Team_Members_Form(instance=member)
      context = {
         'edit_member_form': edit_member_form,
         'member': member
      }
      return render(request, 'admin_panel/edit_member.html', context)

@login_required
def delete_member(request, id):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return redirect('home')
   else:
      member = OurTeam.objects.get(id=id)
      member.delete()
      messages.success(request, 'Member deleted!')
      return redirect('admin_panel:page_content')



