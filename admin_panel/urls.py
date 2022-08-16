from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
   path('', views.dashboard, name='dashboard'),

   # Vehicles
   path('vehicles/', views.vehicles, name='vehicles'),
   path('vehicles/add/', views.add_vehicle, name='add_vehicle'),      
   path('vehicles/edit/<slug:slug>/', views.edit_vehicle, name='edit_vehicle'),
   path('vehicles/delete/<slug:slug>/', views.delete_vehicle, name='delete_vehicle'),

   # Users
   path('users/', views.users, name='users'),
   path('user/<slug:slug>/', views.user_profile, name='user_profile'),   
   path('users/delete/<slug:slug>/', views.delete_user, name='delete_user'),
   
   # Bookings
   path('bookings/', views.bookings, name='bookings'),
   path('confirm_booking/<int:id>/', views.confirm_booking, name='confirm_booking'),
   path('cancel_booking/<int:id>/', views.cancel_booking, name='cancel_booking'),
   path('returned_vehicle/<int:id>/',
        views.vehicle_returned, name='returned_vehicle'),

   # Brands
   path('brands/', views.brands, name='brands'),
   path('delete_brand/<int:id>/', views.delete_brand, name='delete_brand'),
   path('edit_brand/<int:id>/', views.edit_brand, name="edit_brand"),

   # Testimonials
   path('testimonials/', views.testimonials, name='testimonials'),
   path('testimonial/<int:id>/', views.testimonial_detail, name='testimonial_detail'),

   # Subscribers
   path('subscribers/', views.subscribers, name='subscribers'),
   path('delete_subscriber/<int:id>/', views.delete_subscriber, name='delete_subscriber'),
                        
   #Queries
   path('queries/', views.queries, name='queries'),
   path('query/<int:id>/', views.query_detail, name='query_detail'),
   path('delete_query/<int:id>/', views.delete_query, name='delete_query'),

   # Page Content
   path('page_content/', views.page_content, name='page_content'),      
   path('edit_member/<int:id>/', views.edit_member, name='edit_member'),
   path('delete_member/<int:id>/', views.delete_member, name='delete_member'),
]
