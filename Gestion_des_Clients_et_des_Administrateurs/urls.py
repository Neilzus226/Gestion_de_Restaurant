from django.urls import path
from.import views
urlpatterns = [
    #lecture de l'adresse/liste/de la vue
    path('liste/', views.liste_utilisateurs, name='liste_utilisateurs'),
]
