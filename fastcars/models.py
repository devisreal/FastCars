from django.db import models
from django.core.validators import FileExtensionValidator
from cloudinary.models import CloudinaryField

# Create your models here.
class Inquiry(models.Model):
   name = models.CharField(verbose_name="Inquirer's Name", max_length=100)
   email = models.EmailField()
   subject = models.CharField(max_length=200)
   message = models.TextField()
   inqury_date = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return f'Inquiry by {self.name} on {self.inqury_date}'
   
   class Meta:
      ordering = ('-inqury_date',)
      verbose_name = 'Inquirie'


class OurTeam(models.Model):
   name = models.CharField(verbose_name="Team Member's Name", max_length=150)
   position = models.CharField(verbose_name="Position", max_length=100)
   image = CloudinaryField(
      'image',      
      validators=[
         FileExtensionValidator(['jpg', 'jpeg', 'png'])
      ]
   )
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return f'{self.name} - {self.position}'

   class Meta:      
      verbose_name = 'Team Members'


class ContactUsDetails(models.Model):
   address = models.CharField(verbose_name="Company's Address", max_length=200)
   email = models.EmailField(verbose_name="Company's Email")
   phone_no = models.CharField(verbose_name="Company's Phone Number", max_length=20)   

   def __str__(self):
      return f'Contact Us Details'

   class Meta:      
      verbose_name = 'Contact Us Detail'


class Subscriber(models.Model):
   email = models.EmailField()
   subscribed_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return f'{self.email} - {self.subscribed_at}'

   class Meta:      
      verbose_name = 'Subscriber'
      verbose_name_plural = 'Subscribers'