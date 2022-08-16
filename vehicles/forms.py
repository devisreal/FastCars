from django import forms
from .models import Vehicle, Brand, Testimonial, Booking
from datetime import datetime

class VehicleForm(forms.ModelForm):

   vehicle_name = forms.CharField(
      label='Vehicle Name',
      widget=forms.TextInput(
         attrs={
            "placeholder": "",
            "class": "form-control text-md font-medium mb-3",
            "type": "text"
         }
      )
   )   
      
   brand = forms.ModelChoiceField(
      label='Brand',
      queryset=Brand.objects.all(),
      widget=forms.Select(         
         attrs={
            'placeholder': '',
            'class': 'form-control text-md font-medium mb-3',            
         }
      )
   )

   color = forms.CharField(
      label='Color',
      widget=forms.TextInput(
         attrs={
            "placeholder": "",
            "class": "form-control text-md font-medium mb-3",
            "type": "text"
         }
      )
   )

   description = forms.CharField(
      label='Description',
      widget=forms.Textarea(
         attrs={
            'placeholder': '',
            'class': 'form-control text-md font-medium mb-3',
            'id': 'comment',
            'style': 'height: 140px'
         }
      )
   )

   fuel_types = [
      ('Petrol', 'Petrol'),
      ('Diesel', 'Diesel'),
      ('Kerosine', 'Kerosine'),
      ('Electric', 'Electric'),
      ('Hybrid', 'Hybrid'),
   ]

   fuel_type = forms.ChoiceField(
      label='Fuel Type',
      choices=fuel_types,
      widget=forms.Select(         
         attrs={
            'class': 'form-control text-md font-medium mb-3',
         }
      )
   )

   door_choices = [
      ('2', '2'),
      ('4', '4'),
   ]

   doors = forms.ChoiceField(
      label='No of Doors',
      choices=door_choices,
      widget=forms.Select(
          attrs={
              'class': 'form-control text-md font-medium mb-3',
          }
      )
   )

   drive_choices = [
      ('2x2 Drive', '2x2 Drive'),
      ('4x4 Drive', '4x4 Drive'),
   ]

   drive = forms.ChoiceField(
      choices=drive_choices,
      widget=forms.Select(
         attrs={
            'class': 'form-control text-md font-medium mb-3',
         }
      )
   )

   transmission_choices = [
      ('Manual', 'Manual'),
      ('Automatic', 'Automatic'),
   ]

   transmission = forms.ChoiceField(
      choices=transmission_choices,
      widget=forms.Select(
         attrs={
            'class': 'form-control text-md font-medium mb-3',
         }
      )
   )   

   year_choice = []
   for r in range(2000, (datetime.now().year+1)):
      year_choice.append((r, r))

   year = forms.ChoiceField(
      choices=year_choice,
      widget=forms.Select(
         attrs={
            'class': 'form-control text-md font-medium mb-3',
         }
      )
   )

   vin_no = forms.CharField(
      label='Vin No.',
      widget=forms.TextInput(
         attrs={
            "placeholder": "",
            "class": "form-control text-md font-medium mb-3",
            "type": "text"
         }
      )
   )

   price = forms.CharField(
      label='Vehicle Price',
      widget=forms.NumberInput(
         attrs={
            "placeholder": "",
            "class": "form-control text-md font-medium mb-3",
         }
      )
   )

   seats = forms.CharField(
      label='No of Seats',
      widget=forms.NumberInput(
         attrs={
            "placeholder": "",
            "class": "form-control text-md font-medium mb-3",
         }
      )
   )

   horse_power = forms.CharField(
      label='Horse Power',
      widget=forms.NumberInput(
         attrs={
            "placeholder": "",
            "class": "form-control text-md font-medium mb-3",
         }
      )
   )

   mileage = forms.CharField(
      label='Mileage',
      widget=forms.NumberInput(
         attrs={
            "placeholder": "",
            "class": "form-control text-md font-medium mb-3",
         }
      )
   )

   car_photo = forms.ImageField(
      label='Vehicle Image 1',
      widget=forms.FileInput(
         attrs={
            "placeholder": "",
            "class": "form-control text-sm font-medium mb-3",
         }
      )
   )

   car_photo_1 = forms.ImageField(
      label='Vehicle Image 2',
      required=False,
      widget=forms.FileInput(
         attrs={
            "placeholder": "",
            "class": "form-control text-sm font-medium mb-3",
         }
      )
   )

   car_photo_2 = forms.ImageField(
      label='Vehicle Image 3',
      required=False,
      widget=forms.FileInput(
         attrs={
            "placeholder": "",
            "class": "form-control text-sm font-medium mb-3",
         }
      )
   )

   car_photo_3 = forms.ImageField(
      label='Vehicle Image 4',
      required=False,
      widget=forms.FileInput(
         attrs={
            "placeholder": "",
            "class": "form-control text-sm font-medium mb-3",
         }
      )
   )

   class Meta:
      model = Vehicle
      fields = (
         'vehicle_name', 
         'brand', 
         'year',
         'price',
         'color',
         'description',
         'transmission',
         'doors',
         'fuel_type',
         'drive',
         'car_photo',
         'car_photo_1',
         'car_photo_2',
         'car_photo_3',
         'features',
         'seats',
         'vin_no',
         'horse_power',
         'mileage',         
      )
   
   def __init__(self, *args, **kwargs):
      super(VehicleForm, self).__init__(*args, **kwargs)
      self.fields['car_photo'].required = False


class TestimonialForm(forms.ModelForm):

   description = forms.CharField(
      label='',
      widget=forms.Textarea(
         attrs={
            'placeholder': '',
            'class': 'form-control font-semibold text-md bg-gray-100',
            'id': 'description',
            'style': 'height: 150px'
         }
      )
   )

   class Meta:
      model = Testimonial
      fields = ('description',)   


class UpdateTestimonialForm(forms.ModelForm):   

   description = forms.CharField(
      label='',
      widget=forms.Textarea(
         attrs={
            'placeholder': '',
            'readonly':'true',
            'class': 'form-control font-semibold text-md bg-gray-100',
            'id': 'description',
            'style': 'height: 150px'
         }
      )
   )

   is_active = forms.BooleanField(
      label='',
      required=False,
      widget=forms.CheckboxInput(
         attrs={
            'class': 'font-semibold text-md bg-gray-100',
         }
      )
   )

   class Meta:
      model = Testimonial
      fields = ('description', 'is_active')


class BookingForm(forms.ModelForm):

   city = forms.CharField(
      label='',
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white',
         }
      )
   )

   state = forms.CharField(
      label='',
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white',
         }
      )
   )

   pick_up_date = forms.DateTimeField(
      label='',
      widget=forms.DateInput(
         attrs={
            'type': 'datetime-local',
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white',
         }
      )
   )

   drop_off_date = forms.DateTimeField(
      label='',
      widget=forms.DateInput(
         attrs={
            'type': 'datetime-local',
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white',
         }
      )
   )

   class Meta:
      model = Booking
      fields = ('city', 'state', 'pick_up_date', 'drop_off_date')   