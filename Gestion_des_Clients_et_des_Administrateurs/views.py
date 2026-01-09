from django.shortcuts import render, redirect,get_object_or_404

# Create your views here.
from django.db.models import Q
from .models import Profil

#code Python de "Ajouter un utilisateur"
from django.db.models import Q
from .models import Profil

def liste_utilisateurs(request):
    query = request.GET.get('q', '')
    utilisateurs = Profil.objects.select_related("user").all().order_by('-id')
    
    if query:
        utilisateurs = utilisateurs.filter(
            Q(user__email__icontains=query) |
            Q(user__nom__icontains=query) |
            Q(user__prenom__icontains=query) |
            Q(role__icontains=query) |
            Q(telephone__icontains=query)
        )
    
    return render(request, "gestion/liste_utilisateurs.html", {
        "utilisateurs": utilisateurs,
        "query": query
    })
#ajout d'un utilisateur(serveur de base)
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import Profil  # Remplacez 'Profil' par le nom exact de votre modèle

User = get_user_model()


from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

User = get_user_model()

def utilisateur_add(request):
    if request.method == "POST":
        # Récupération des données
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        tel = request.POST.get('telephone')
        email = request.POST.get('email')
        mdp = request.POST.get('password')
        role = request.POST.get('role')

        # Vérification si l'utilisateur existe déjà
        if User.objects.filter(email=email).exists():
            return render(request, 'ajouter_utilisateur.html', {
                'erreur': "Cet email est déjà utilisé."
            })

        try:
            # Création de l'utilisateur
            nouvel_user = User.objects.create_user(
                email=email,
                password=mdp,
                nom=nom,
                prenom=prenom,
                telephone=tel
            )

            # Ajout du rôle si ton modèle CustomUser a ce champ
            nouvel_user.role = role
            nouvel_user.save()

            # Redirection vers la liste
            return redirect('Gestion_des_Clients_et_des_Administrateurs:liste_utilisateurs')

        except Exception as e:
            return render(request, 'ajouter_utilisateur.html', {
                'erreur': f"Une erreur est survenue : {e}"
            })

    return render(request, 'ajouter_utilisateur.html')
#code Python de "Modifier un utilisateur"  
def modifier_utilisateur(request,id):
    profil = get_object_or_404(Profil, id=id)
    if request.method == 'POST':
        profil.role = request.POST.get("role", profil.role)
        profil.telephone = request.POST.get("telephone", profil.user.username)
        profil.user.set_password(request.POST.get("password",profil.user.password))
        profil.user.save()
        profil.save()
        return redirect("liste_utilisateurs")
    return render(request,"gestion/modifier_utilisateur.html",{'profil':profil})
    
#code python de "supprimer utilisateur"
def supprimer_utilisateur(request,id):    
    profil = get_object_or_404(Profil, id=id)
    profil.user.delete()
    profil.delete()
    return redirect('liste_utilisateurs')    