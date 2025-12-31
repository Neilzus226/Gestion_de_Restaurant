from django.urls import path
from . import views

urlpatterns = [
    path('',views.liste_plats, name='liste_plats'),
    path('ajouter',views.ajouter_plat, name='ajouter_plat'),
    path('modifier/<int:pk>/',views.modifier_plat, name='modifier_plat'),
    path('supprimer/<int:pk>/',views.supprimer_plat, name='supprimer_plat'),
]