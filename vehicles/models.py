from django.db import models
from datetime import datetime
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from django.template.defaultfilters import slugify
from accounts.models import User
from cloudinary.models import CloudinaryField
# Create your models here.


class Brand(models.Model):
   name = models.CharField(max_length=100)   
   created_at = models.DateTimeField(auto_now_add=True)   

   def __str__(self):
      return self.name

class Vehicle(models.Model):

   features_choices = (      
      ('Audio Input', 'Audio Input'),      
      ('Air Conditioning', 'Air Conditioning'),
      ('Heated seats', 'Heated seats'),
      ('Alarm System', 'Alarm System'),                        
      ('Bluetooth', 'Bluetooth'),
      ('GPS Navigation', 'GPS Navigation'),
      ('Parking Sensors', 'Parking Sensors'),      
      ('Rear View Camera', 'Rear View Camera'),      
      ('USB input', 'USB input'),
      ('FM Radio', 'FM Radio'),
      ('Remote central locking', 'Remote central locking'),
      ('Child Seat', 'Child Seat'),
      ('Wifi Access', 'Wifi Access'),
   )

   door_choices = (
      ('2', '2'),      
      ('4', '4'),      
   )

   drive = (
      ('2x2 Drive', '2x2 Drive'),
      ('4x4 Drive', '4x4 Drive'),
   )

   transmission = (
      ('Manual', 'Manual'),
      ('Automatic', 'Automatic'),
   )

   fuel_type = (
      ('Petrol', 'Petrol'),
      ('Diesel', 'Diesel'),
      ('Kerosine', 'Kerosine'),
      ('Electric', 'Electric'),
      ('Hybrid', 'Hybrid'),
   )   

   year_choice = []
   for r in range(2000, (datetime.now().year+1)):
      year_choice.append((r, r))

   vehicle_name = models.CharField(max_length=150, unique=True)
   brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
   year = models.PositiveIntegerField(choices=year_choice)
   price = models.PositiveIntegerField()
   color = models.CharField(max_length=20)
   description = RichTextField()
   horse_power = models.PositiveIntegerField(blank=True)
   transmission = models.CharField(choices=transmission, max_length=20)
   doors = models.CharField(choices=door_choices, max_length=10)
   fuel_type = models.CharField(choices=fuel_type, max_length=20)
   drive = models.CharField(choices=drive, max_length=15)
   car_photo = CloudinaryField(
      'image',
      validators=[
         FileExtensionValidator(
            ['jpg', 'jpeg', 'png']
         )
      ],       
   )

   car_photo_1 = CloudinaryField(
      'image',
      validators=[
         FileExtensionValidator(
            ['jpg', 'jpeg', 'png']
         )
      ],       
      null=True,
      blank=True
   )

   car_photo_2 = CloudinaryField(
      'image',
      validators=[
         FileExtensionValidator(
            ['jpg', 'jpeg', 'png']
         )
      ],       
      null=True,
      blank=True
   )

   car_photo_3 = CloudinaryField(
      'image',
      validators=[
         FileExtensionValidator(
            ['jpg', 'jpeg', 'png']
         )
      ],       
      null=True,
      blank=True
   )  

   features = MultiSelectField(choices=features_choices, blank=True)
   seats = models.PositiveIntegerField()
   vin_no = models.CharField(max_length=17)
   mileage = models.PositiveIntegerField(blank=True)
   is_booked = models.BooleanField(default=False, blank=True)
   created_date = models.DateTimeField(auto_now_add=True)
   updated_date = models.DateTimeField(auto_now=True)
   slug = models.SlugField(null=True, blank=True)

   def __str__(self):
      return self.vehicle_name

   def save(self, *args, **kwargs):
      self.slug = slugify(self.vehicle_name)
      super().save(*args, **kwargs)

class Testimonial(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="testimonials")
   description = models.TextField()
   created_date = models.DateTimeField(auto_now_add=True)
   is_active = models.BooleanField(default=False, blank=True)

   def __str__(self):
      return f'{self.user.username} on {self.vehicle.vehicle_name}'


class Booking(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="bookings")
   city = models.CharField(max_length=100)
   state = models.CharField(max_length=100)
   pick_up_date = models.DateTimeField()
   drop_off_date = models.DateTimeField()
   booking_date = models.DateTimeField(auto_now_add=True)
   is_active = models.BooleanField(default=False, blank=True)
   vehicle_returned = models.BooleanField(default=False, blank=True)
   is_completed = models.BooleanField(default=False, blank=True)
   
   class Meta:
      ordering = ['-booking_date']

   def __str__(self):
      return f'{self.user.username} on {self.vehicle.vehicle_name}'