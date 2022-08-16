from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField

# Create your models here.

class User(AbstractUser):
   profile_image = CloudinaryField(
      'image',
      blank=True,
      validators=[
         FileExtensionValidator(
            allowed_extensions=[
               'png', 'jpg', 'jpeg'
            ]
         )
      ]
   )
   address = models.CharField(max_length=200, blank=True)
   phone_no = models.CharField(max_length=14, blank=True)
   slug = models.SlugField(null=True, blank=True, max_length=255)

   def __str__(self):
      return f'{self.username}'

   def save(self, *args, **kwargs):
      self.slug = slugify(self.username)
      super().save(*args, **kwargs)
