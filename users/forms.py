from typing import Any
from django import forms
from accounts.models import User


class EditProfileForm(forms.ModelForm):
   
   username = forms.CharField(
      label='',
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white',
         }
      )
   )

   first_name = forms.CharField(
      label='',
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white',
         }
      )
   )

   last_name = forms.CharField(
      label='',
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white',
         }
      )
   )

   profile_image = forms.ImageField(
      label='',
      required=False,
      widget=forms.FileInput(
         attrs={
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white',
         }
      )
   )

   email = forms.EmailField(
      label='Email',
      widget=forms.EmailInput(
         attrs={
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white'
         }
      ),
   )

   phone_no = forms.CharField(
      label='',
      required=False,
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white',
         }
      )
   )

   address = forms.CharField(
      label='',
      required=False,
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white',
         }
      )
   )

   
   class Meta:
      model = User
      fields = ('username', 'first_name', 'last_name', 'profile_image','email', 'phone_no', 'address' )      
   
   def __init__(self, *args: Any, **kwargs: Any) -> None:
      super(EditProfileForm , self).__init__(*args, **kwargs)

      for fieldname in ('username', 'first_name', 'last_name', 'profile_image','email', 'phone_no', 'address' ):
         self.fields[fieldname].help_text = None

