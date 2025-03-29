# reservations/sms_service.py
from django.conf import settings
from twilio.rest import Client
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Email,Mail,Personalization,To, From
from sendgrid.helpers.mail import Mail, Email, From, Personalization, To
from django.conf import settings
from sendgrid import SendGridAPIClient

def format_french_phone_number(number: str) -> str:
    # Enlève les espaces, tirets, etc.
    cleaned = ''.join(filter(str.isdigit, number))
    # Si le numéro commence par 0, remplace par +33
    if cleaned.startswith("0"):
        return "+33" + cleaned[1:]
    return cleaned  # Sinon on considère que c'est déjà international


def send_sms(to_number, message):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    
    try:
        formatted_number = format_french_phone_number(to_number)
        sms = client.messages.create(
            body=message,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=formatted_number
        )
        print(f"✅ SMS envoyé avec SID : {sms.sid} Status {sms.status}")
        return True
    except Exception as e:
        print(f"❌ Erreur d'envoi de SMS: {str(e)}")
        return False




def send_email(to_mail, dynamic_data, template_id="d-bc98caa0713545fd9bbff6be377070ee", subject="Reservation Carlina Confirmée"):
    try:
        
        # Utiliser To() au lieu de Email()
        to_email = To(to_mail)
        
        # Créer le message
        message = Mail(
            from_email=From(settings.DEFAULT_FROM_EMAIL, "Carlina Restaurant")
        )
        
        # Créer une personnalisation
        personalization = Personalization()
        
        # Ajouter explicitement le destinataire à la personnalisation
        personalization.add_to(to_email)
        personalization.dynamic_template_data = {} 
        personalization.dynamic_template_data = dynamic_data
        
        # Ajouter la personnalisation au message
        message.add_personalization(personalization)
        
        # Définir l'ID du template
        message.template_id = template_id

        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        
        print("✅ E-mail envoyé ! Code de statut :", response.status_code)
        return True
    
    except Exception as e:
        print("❌ Erreur d'envoi :", str(e))
        return False