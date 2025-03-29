# reservations/views.py
from rest_framework import status
from django.core.mail import send_mail
from rest_framework.response import Response
from .models import Reservation
from .serializer import ReservationSerializer
from .sms_service import send_email,send_sms
from django.conf import settings
from rest_framework.decorators import api_view




@api_view(['POST'])
def create_reservation(request):
    print(request.data)
    serializer = ReservationSerializer(data=request.data)
    
    if serializer.is_valid():
        # Sauvegarder la réservation
        reservation = serializer.save()
        print("Serialize valid")
        # Préparer les données dynamiques pour le template
        phone=reservation.phone
        dynamic_data = {
            'client_name': reservation.name,
            'reservation_date': reservation.date_time.strftime('%d/%m/%Y'),
            'reservation_time': reservation.date_time.strftime('%H:%M'),
            'reservation_message': reservation.message or 'Aucune demande spéciale',
            'nombre_personne':str(reservation.nombre_personne)
        }
        print(reservation.email)
        # Envoyer l'email avec les données dynamiques
        if send_email(reservation.email, dynamic_data):
            print("Mail Envoyé")
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
