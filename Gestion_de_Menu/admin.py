from django.contrib import admin
from .models import Plat 

@admin.register(Plat)
class PlatAdmin(admin.ModelAdmin):
    list_display = ('id_plat', 'nom', 'categorie', 'prix')
    search_fields = ['nom']

# Register your models here.
