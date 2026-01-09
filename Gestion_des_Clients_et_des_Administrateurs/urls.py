from django.urls import path
from . import views
app_name="Gestion_des_Clients_et_des_Administrateurs"
urlpatterns = [
    #lecture de l'adresse/liste/de la vue
    path('liste/', views.liste_utilisateurs, name='liste_utilisateurs'),
]
