# reservations/serializers.py
from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'name', 'email', 'phone', 'date_time', 'message', 'created_at','nombre_personne']
        read_only_fields = ['id', 'created_at']