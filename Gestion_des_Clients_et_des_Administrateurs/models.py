from django.db import models 

# Create your models here.
from django.contrib.auth.models import User 
class Profil(models.Model):
#on lit ce profil à un compte utilisateur Django
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    #Définition des deux rôles
    ROLE_CHOICES = [('ADMIN','Administrateur'),('CLIENT','Client'),]
    role = models.CharField(max_length=10,choices=ROLE_CHOICES, default='CLIENT')
    telephone = models.CharField(max_length=20,blank=True)
    def __str__(self):
        return f"{self.user.username}({self.role})"    

