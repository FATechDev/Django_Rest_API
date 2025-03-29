from django.db import models

# Create your models here.



class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default="mohamedahmim@icloud.com")
    nombre_personne=models.IntegerField(default=1)
    phone = models.CharField(max_length=20)
    date_time = models.DateTimeField()
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.date_time}"
