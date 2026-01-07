from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


# =======================
# INSCRIPTION
# =======================
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "nom",
            "prenom",
            "telephone",
            "email",
            "password1",
            "password2",
        )
        widgets = {
            "nom": forms.TextInput(attrs={"class": "form-control"}),
            "prenom": forms.TextInput(attrs={"class": "form-control"}),
            "telephone": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data.get("email")
        user.nom = self.cleaned_data.get("nom")
        user.prenom = self.cleaned_data.get("prenom")
        user.telephone = self.cleaned_data.get("telephone")

        if commit:
            user.save()

        return user


# =======================
# MODIFICATION DU PROFIL
# =======================
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "nom",
            "prenom",
            "telephone",
            "email",
        )
        widgets = {
            "nom": forms.TextInput(attrs={"class": "form-control","readonly":True}),
            "prenom": forms.TextInput(attrs={"class": "form-control","readonly":True}),
            "telephone": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }
