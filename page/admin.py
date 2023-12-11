from django.contrib import admin
from .models import *
from accounts.models import *

#On definit les attributs qu'on veut afficher pour l'administrateur par une autre manière
@admin.register(Etablissement)
class AdminEtablissemennt(admin.ModelAdmin):
    list_display = ("name","langue", "latitude", "longitude", "categorie", "type")
    # liste des tuples à afficher
    list_per_page = 7
@admin.register(Suggestion)
class AdminSuggestion(admin.ModelAdmin):
    list_display = ("titre","contenu")
    # liste des tuples à afficher
    list_per_page = 7

#on importe la table créée pour l'administrateur
admin.site.register(CustomUser)
admin.site.register(Categorie)
admin.site.register(Cycle)
admin.site.register(Type)
admin.site.register(Composer)