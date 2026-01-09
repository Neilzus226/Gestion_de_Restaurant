from django.urls import path
from . import views
app_name='Gestion_de_Menu'
urlpatterns = [
    path('',views.liste_plats, name='liste_plats'),
    path('tableau_de_bord/', views.tableau_de_bord, name='tableau_de_bord'),
    path('ajouter',views.ajouter_plat, name='ajouter_plat'),
    path('modifier/<int:pk>/',views.modifier_plat, name='modifier_plat'),
    path('supprimer/<int:pk>/',views.supprimer_plat, name='supprimer_plat'),
    path('base',views.base, name='base'),
]