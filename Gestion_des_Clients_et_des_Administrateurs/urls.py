from django.urls import path
from . import views
app_name="Gestion_des_Clients_et_des_Administrateurs"
urlpatterns = [
    #lecture de l'adresse/liste/de la vue
    #path('liste/', views.liste_utilisateurs, name='liste_utilisateurs'),
    path('utilisateur/Ajouter/', views.utilisateur_add, name='utilisateur_add'),
    path('utilisateurs/utilisateur/Modifier/<int:id>/', views.modifier_utilisateur, name="utilisateur_edit"),
    path('utilisateurs/utilisateur/Supprimer/<int:id>/', views.supprimer_utilisateur, name='utilisateur_delete'),
    path('utilisateurs/', views.liste_utilisateurs,name='liste_utilisateurs'),
    
]
