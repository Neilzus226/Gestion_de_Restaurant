from django.urls import path
from . import views
urlpatterns = [
    #lecture de l'adresse/liste/de la vue
    path('liste/', views.liste_utilisateurs, name='liste_utilisateurs'),
    path('utilisateur/AJOUTER/',views.AJOUTER_utilisateur, name='utilisateur_add'),
    path('utilisateur/MODIFIER/<int:id>/', views.MODIFIER_utilisateur, name='utilisateur_edit'),
    path('utilisateur/SUPPRIMER/<int:id>/', views.SUPPRIMER_utilisateur, name='utilisateur_delete'),
]
