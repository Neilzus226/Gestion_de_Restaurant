from django.urls import path
from . import views

app_name="Gestion_de_Vente"

urlpatterns = [
    
    path('',views.liste_ventes,name='liste_ventes'),
    path('ajouter/',views.ajouter_vente,name='ajouter_vente'),
     path("ventes/modifier/<int:vente_id>/", views.modifier_vente, name="modifier_vente"),
    path("ventes/supprimer/<int:vente_id>/", views.supprimer_vente, name="supprimer_vente"),
]


