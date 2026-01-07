from django.urls import path
from . import views
urlpatterns = [
    #lecture de l'adresse/liste/de la vue
    path('liste/', views.liste_utilisateurs, name='liste_utilisateurs'),
    path('utilisateur/Ajouter/',views.Ajouter_utilisateur, name='utilisateur_add'),
    path('utilisateur/Modifier/<int:id>/', views.Modifier_utilisateur, name='utilisateur_edit'),
    path('utilisateur/Supprimer/<int:id>/', views.Supprimer_utilisateur, name='utilisateur_delete'),
]
