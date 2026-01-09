from django.shortcuts import render, redirect,get_object_or_404

# Create your views here.
from django.db.models import Q
from .models import Profil

#code Python de "Ajouter un utilisateur"
def liste_utilisateurs(request): 
    query = request.GET.get('q', '')
    utilisateurs = Profil.objects.select_related("user").all().order_by('-id')
    
    if query:
        utilisateurs = utilisateurs.filter(
            Q(user__username__icontains=query)|
            Q(role__icontains=query)|
            Q(telephone__icontains=query))
    return render(request, "gestion/liste_utilisateurs.html",{"utilisateurs": utilisateurs,'query':query})

#ajout d'un utilisateur(serveur de base)
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profil  # Remplacez 'Profil' par le nom exact de votre modèle

def utilisateur_add(request):
    if request.method == "POST":
        # 1. On récupère les données saisies dans le formulaire HTML
        nom = request.POST.get('username')
        mdp = request.POST.get('password')
        role = request.POST.get('role')
        tel = request.POST.get('telephone')

        # 2. Sécurité : On vérifie si l'utilisateur existe déjà
        if User.objects.filter(username=nom).exists():
            return render(request, 'ajouter_utilisateur.html', {
                'erreur': "Ce nom d'utilisateur est déjà pris."
            })

        try:
            # 3. Création de l'utilisateur dans la table de base de Django (Auth User)
            nouvel_user = User.objects.create_user(username=nom, password=mdp)

            # 4. Création du profil associé (votre table personnalisée)
            Profil.objects.create(
                user=nouvel_user, 
                role=role, 
                telephone=tel
            )

            # 5. LA REDIRECTION : On renvoie vers la page de la liste
            # Assurez-vous que 'liste_utilisateurs' est le 'name' dans votre urls.py
            return redirect('utilisateur_add')

        except Exception as e:
            # En cas d'erreur imprévue
            return render(request, 'ajouter_utilisateur.html', {
                'erreur': f"Une erreur est survenue : {e}"
            })

    # Si c'est une requête GET (affichage simple de la page)
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