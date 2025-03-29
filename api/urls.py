from django.urls import path 
from .views import create_reservation


urlpatterns = [
    path('reservations/', create_reservation, name='reservation-create'),
]