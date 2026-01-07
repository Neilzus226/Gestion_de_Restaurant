from django.shortcuts import render

# Create your views here.
from .models import Profil

#code Python de "Ajouter un utilisateur"
def liste_utilisateurs(request): 
    utilisateurs = Profil.objects.all()
    return render(request, 'gestion/liste_utilisateurs.html',{'utilisateurs': utilisateurs})
#ajout d'un utilisateur(serveur de base)
from django.contrib.auth.models import User
from .models import Profil
def ajouter_utilisateur(request):
    if request.method == 'POSt':
        user = User.objects.create_user(
username=request.POST['username'],
password=request.POST['password'])
        Profil.objects.create(user=user,
role=request.POST['role'],
telephone=request.POST['telephone'])
        return redirect('liste_utilisateurs')
    return render(request,'gestion/ajouter_utilisateur.html')  

#code Python de "Modifier un utilisateur"  
def modifier_utilisateur(request,id):
    profil = Profil.objects.get(id=id)
    if request.method == 'POST':
        profil.role = request.POST['role']
        profil.telephon = request.POST['telephone']
        profil.save()
        return redirect('liste_utilisateurs')
        return render(request,'gestion/modifier_utilisateur.html',{'profil':profil})
    
#code python de "supprimer utilisateur"
def supprimer_utilisateur(request,id):
    profil = Profil.objects.get(id=id)
    return redirect('liste_utilisateur')    