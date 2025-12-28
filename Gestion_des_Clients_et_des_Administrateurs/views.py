from django.shortcuts import render

# Create your views here.
from.models import Profil
def liste_utilisateurs(request): 
    utilisateurs = Profil.objects.all()
    return render(request, 'gestion/liste_utilisateurs.html',{'utilisateurs': utilisateurs})