from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Plat
from .forms import PlatForm# Vue pour afficher la liste et rechercher
def liste_plats(request):
    query = request.GET.get('search')
    if query:
        plats = Plat.objects.filter(nom__icontains=query) 
    else:
        plats = Plat.objects.all()
    return render(request, 'Gestion_de_Menu/menu_list.html', {'plats': plats})

# Vue pour ajouter un plat
def ajouter_plat(request):
    if request.method == "POST":
        form = PlatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_plats')
    else:
        form = PlatForm()
    return render(request, 'Gestion_de_Menu/ajouter_plat.html', {'form': form})

# Vue pour supprimer un plat
def modifier_plat(request,pk):
    plat = get_object_or_404(Plat, pk=pk)
    if request.method == "POST":
        form = PlatForm(request.POST, instance=plat)
        if form.is_valid():
            form.save()
            return redirect('liste_plats')
    else:
        form = PlatForm(instance=plat)
    return render(request, 'Gestion_de_Menu/ajouter_plat.html', {'form': form,'edit_mode':True})

# Vue pour ajouter un plat
def supprimer_plat(request, pk):
    plat = get_object_or_404(Plat, pk=pk)
    if request.method == "POST":
        plat.delete()
        return redirect('liste_plats')
    return render(request, 'Gestion_de_Menu/supprimer_plat.html', {'plat': plat})

# Create your views here.
