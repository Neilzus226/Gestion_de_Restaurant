from django.db import models 

# Create your models here.
from django.conf import settings  
class Profil(models.Model):
#on lit ce profil à un compte utilisateur Django
    user= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #Définition des deux rôles
    ROLE_CHOICES = [('ADMIN','Administrateur'),('CLIENT','Client'),]
    role = models.CharField(max_length=20,choices=ROLE_CHOICES, default='CLIENT')
    telephone = models.CharField(max_length=15,blank=True, null=True)
    

