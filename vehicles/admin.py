from django.contrib import admin
from .models import Brand, Vehicle, Testimonial, Booking

# Register your models here.
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
   list_display = ('name', 'created_at')   
   search_fields = ('name',)   
   

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
   list_display = ('vehicle_name', 'brand', 'year', 'price', 'color')
   search_fields = ('vehicle_name', 'year',)   
   list_per_page = 10

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
   pass       

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
   pass