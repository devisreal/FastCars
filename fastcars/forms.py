from django import forms
from .models import ContactUsDetails, OurTeam


class Contact_Details_Form(forms.ModelForm):

   address = forms.CharField(
      label='',
      widget=forms.TextInput(
        attrs={
          "placeholder": "",
          "class": "form-control text-md font-medium",          
          "type":"text"
        }
      )
   )

   email = forms.EmailField(
      label='',
      widget=forms.EmailInput(
         attrs={
            "type": "email",
            "placeholder": "",
            "class": "form-control text-md font-medium",            
         }
      )
   )

   phone_no = forms.CharField(
      widget=forms.NumberInput(
         attrs={
            "placeholder": "Phone Number",
            "class": "form-control text-md font-medium",
            "type": "tel"
         }
      )
   )

   class Meta:
      model = ContactUsDetails
      fields = ('address', 'email', 'phone_no', )


class Team_Members_Form(forms.ModelForm):

   name = forms.CharField(
      label='',
      widget=forms.TextInput(
         attrs={
            "placeholder": "",
            "class": "form-control text-md font-medium",            
         }
      )
   )

   position = forms.CharField(
      label='',
      widget=forms.TextInput(
         attrs={
            "placeholder": "",
            "class": "form-control text-md font-medium",            
         }
      )
   )

   image = forms.ImageField(
      label='',
      widget=forms.FileInput(
         attrs={
            "placeholder": "",
            "class": "form-control text-sm mt-2 font-medium",
         }
      )
   )

   class Meta:
      model = OurTeam
      fields = ('name', 'position', 'image', )