from django.db import models
from Gestion_de_Menu.models import Plat

class Vente(models.Model):
    plat=models.ForeignKey(Plat,on_delete=models.CASCADE)
    quantite=models.PositiveBigIntegerField()
    date_vente=models.DateTimeField(auto_now_add=True)
    prix_total=models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return f"Vente de {self.plat.nom} - {self.quantite} unités"
