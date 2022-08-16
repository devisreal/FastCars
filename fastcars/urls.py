from django.urls import path
from . import views
from vehicles.views import vehicles, vehicle_details, search_vehicles

urlpatterns = [
    # Pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('footer/', views.footer, name='footer'),

    # Vehicles
    path('vehicles/', vehicles, name='vehicles'),
    path('vehicle/<slug:slug>/', vehicle_details, name='vehicle_details'),
        

    # Search
    path('search/', search_vehicles, name='search'),
    
]
