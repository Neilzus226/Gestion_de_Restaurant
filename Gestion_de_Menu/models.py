from django.db import models
class Plat(models.Model):
    CATEGORIES = [
        ('Entrée','Entrée'),
        ('Plat principal','Plat principal'),
        ('Dessert','Dessert'),
        ('Boisson','Boisson'),
    ]
    id_plat = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    categorie = models.CharField(max_length=50, choices=CATEGORIES)
    prix = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to = 'plats/', null=True, blank=True)

    def __str__(self):
        return self.nom
class Vente(models.Model):
    plat = models.ForeignKey('Plat', on_delete=models.CASCADE, related_name='ventes_menu')
    quantite = models.PositiveIntegerField(default=1)
    date_vente = models.DateTimeField(auto_now_add=True)
    total_prix = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.quantite} x {self.plat.nom}"
# Create your models here.
