from django.contrib import admin
# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Champs affichés dans la liste des utilisateurs
    list_display = ("email", "nom", "prenom", "telephone", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")

    # Champs affichés dans le formulaire de modification
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Informations personnelles", {"fields": ("nom", "prenom", "telephone")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
    )

    # Champs affichés dans le formulaire de création
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "nom", "prenom", "telephone", "password1", "password2", "is_staff", "is_active"),
        }),
    )

    search_fields = ("email", "nom", "prenom", "telephone")
    ordering = ("email",)

# Enregistrement du modèle dans l’admin
admin.site.register(CustomUser, CustomUserAdmin)
