from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import SignUpForm, ProfileUpdateForm


# =======================
# INSCRIPTION
# =======================
def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # connexion automatique
            messages.success(request, "Compte créé avec succès")
            return redirect("accounts:profile")
    else:
        form = SignUpForm()

    return render(request, "signup.html", {"form": form})


# =======================
# CONNEXION
# =======================
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect("accounts:nav")
        else:
            messages.error(request, "Email ou mot de passe incorrect")

    return render(request, "login.html")


# =======================
# PROFIL UTILISATEUR
# =======================
@login_required(login_url="accounts:login")
def profile_view(request):
    return render(request, "profile.html")


# =======================
# MODIFIER LE PROFIL
# =======================
@login_required(login_url="accounts:login")
def profile_edit(request):
    user = request.user

    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profil modifié avec succès")
            return redirect("accounts:profile")
    else:
        form = ProfileUpdateForm(instance=user)

    return render(request, "profile_edit.html", {"form": form})


# =======================
# SUPPRIMER LE PROFIL
# =======================
@login_required(login_url="accounts:login")
def profile_delete(request):
    if request.method == "POST":
        request.user.delete()
        logout(request)
        messages.success(request, "Compte supprimé avec succès")
        return redirect("accounts:home")

    return render(request, "profile_delete.html")


# =======================
# NAVBAR / ESPACE PROTÉGÉ
# =======================
@login_required(login_url="accounts:login")
def nav(request):
    return render(request, "nav.html")


# =======================
# PAGE D'ACCUEIL
# =======================
def home(request):
    return render(request, "home.html")
