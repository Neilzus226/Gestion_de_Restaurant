# accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views

from .views import signup_view, login_view,nav,home,profile_view,profile_edit, profile_delete

app_name = "accounts"

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
     path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"), 
    path("nav/", nav, name="nav"),
     path("home/", home, name="home"),
    path("profile/", profile_view, name="profile"),
    path("profile/edit/", profile_edit, name="profile_edit"),
    path("profile/delete/", profile_delete, name="profile_delete"),


]