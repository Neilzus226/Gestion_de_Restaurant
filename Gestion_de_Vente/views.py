from django.shortcuts import render,redirect,get_object_or_404
from .models import Vente
from Gestion_de_Menu.models import Plat
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa




def liste_ventes(request):
    ventes=Vente.objects.all().order_by('-date_vente')
    return render(request, 'liste_ventes.html', {'ventes': ventes})


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Vente
from Gestion_de_Menu.models import Plat

def ajouter_vente(request):
    if request.method == "POST":
        plat_id = request.POST.get("plat")
        quantite = request.POST.get("quantite")
 
        # Vérification : si vide
        if not plat_id or not quantite:
            plats = Plat.objects.all()
            return render(request, "ajouter_vente.html", {
                "plats": plats,
                "error": "Veuillez sélectionner un plat et entrer une quantité."
            })

        try:
            plat = Plat.objects.get(pk=int(plat_id))
            prix_total = plat.prix * int(quantite)

            Vente.objects.create(
                plat=plat,
                quantite=int(quantite),
                prix_total=prix_total
            )
            messages.success(request, "Vente enregistrée avec succès !")
            return redirect("Gestion_de_Vente:liste_ventes")

        except Plat.DoesNotExist:
            messages.error(request, "Plat introuvable.")
            return redirect("Gestion_de_Vente:ajouter_vente")

    plats = Plat.objects.all()
    return render(request, "ajouter_vente.html", {"plats": plats})

def modifier_vente(request, vente_id):
    vente = get_object_or_404(Vente, pk=vente_id)
    plats = Plat.objects.all()

    if request.method == "POST":
        plat_id = request.POST.get("plat")
        quantite = request.POST.get("quantite")

        if not plat_id or not quantite:
            messages.error(request, "Veuillez remplir tous les champs.")
        else:
            plat = Plat.objects.get(pk=int(plat_id))
            vente.plat = plat
            vente.quantite = int(quantite)
            vente.prix_total = plat.prix * int(quantite)
            vente.save()
            messages.success(request, "Vente modifiée avec succès !")
            return redirect("Gestion_de_Vente:liste_ventes")

    return render(request, "modifier_vente.html", {"vente": vente, "plats": plats})


def supprimer_vente(request, vente_id):
    vente = get_object_or_404(Vente, pk=vente_id)
    vente.delete()
    messages.success(request, "Vente supprimée avec succès !")
    return redirect("Gestion_de_Vente:liste_ventes")


def enregistrer_vente(request, plat_id):
    plat = get_object_or_404(Plat, pk=plat_id)
    quantite = int(request.POST.get("quantite", 1))
    prix_total = plat.prix * quantite

    vente = Vente.objects.create(plat=plat, quantite=quantite,prix_total=prix_total)

    # Redirection vers la facture PDF
    return redirect("Gestion_de_Vente:facture_pdf", vente_id=vente.id)

