from django.urls import path
from .views import dashboard, my_bookings, user_logout, edit_profile, change_password, my_testimonies

app_name = 'users'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('my_bookings/', my_bookings, name='my_bookings'),
    path('my_testimonies/', my_testimonies, name='my_testimonies'),
    path('edit_profile/', edit_profile, name='edit_profile'),    
    path('change_password', change_password, name='change_password'),
    path('logout/', user_logout, name='logout')
]
