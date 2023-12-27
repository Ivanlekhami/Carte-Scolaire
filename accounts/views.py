from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib import messages
from page.models import *

# Create your views here.
User = get_user_model()
def register(request):
    if request.method == "POST":
        #recuperation des informations issues du formulaire
        username = request.POST.get("username")
        password = request.POST.get("password")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        #verification des champs entrés
        if User.objects.filter(username=username):
            messages.error(request, "Ce nom d'utilisateur existe déjà")
            return redirect("register")
        if User.objects.filter(email=email):
            messages.error(request, "Cet email a déjà un compte")
            return redirect("register")
        #créer un compte pour l'utilisateur
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        messages.success(request, "Le compte a été crée avec succès")
        return redirect("register")
    return render(request, "register.html")

#connecter l'utilisateur
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        #verifier si les information existent dans la BD
        if user:
            login(request, user)
            return redirect("administrate")
        else:
            messages.error(request, "Compte introuvable ou erreur lors de la saisie")
            return redirect("login")
    return render(request, "login.html")

#déconnecter l'utilisateur
def logout_user(request):
    logout(request)
    return redirect("login")

def administrate(request):
    admin = User.objects.all()
    ets = Etablissement.objects.all()
    suggestion = Suggestion.objects.all()
    context = {"admin": admin, "ets": ets, "suggestion": suggestion}
    return render(request, "administrate.html", context)
def ajout_etab(request):
    type = Type.objects.all()
    categorie = Categorie.objects.all()
    if request.method == "POST":
        #recuperation des informations issues du formulaire
        name = request.POST.get("name")
        langue = request.POST.get("langue")
        longitude = request.POST.get("longitude")
        latitude = request.POST.get("latitude")
        #recuperation de l'id des clés etrangères
        type = Type.objects.get(name=request.POST.get("type"))
        type = type.id
        type = Type.objects.get(id=type)
        categorie = Categorie.objects.get(name=request.POST.get("categorie"))
        categorie = categorie.id
        categorie = Categorie.objects.get(id=categorie)
        #verification des champs entrés
        if Etablissement.objects.filter(latitude=latitude, longitude=longitude):
            messages.error(request, "Ces coordonnées existent déjà!")
            return redirect("ajout_etab")
        #Insertion dans la base de données
        new = Etablissement.objects.create(name=name, langue=langue, latitude=latitude,
                                           longitude=longitude, type=type, categorie=categorie)
        new.save()
        messages.success(request, "Ecole a été ajoutée")
        return redirect("ajout_etab")
    return render(request, "ajout_etab.html", {"types": type, "categorie": categorie})
def modifier(request, ecole_id=None):
    types = Type.objects.all()
    categories = Categorie.objects.all()
    if request.method == 'POST':
        if ecole_id is not None:
            ecole_cible = Etablissement.objects.get(id=ecole_id)
            ecole_cible.name = request.POST.get("name")
            ecole_cible.langue = request.POST.get("langue")
            ecole_cible.latitude = request.POST.get("latitude")
            ecole_cible.longitude = request.POST.get("longitude")
            # recuperation de l'id des clés etrangères
            type = Type.objects.get(name=request.POST.get("type"))
            type = type.id
            type = Type.objects.get(id=type)
            categorie = Categorie.objects.get(name=request.POST.get("categorie"))
            categorie = categorie.id
            categorie = Categorie.objects.get(id=categorie)
            ecole_cible.categorie = categorie
            ecole_cible.type = type
            ecole_cible.save()
            messages.success(request, "Etablissement a été modifié")
            return render(request, "modifier.html", {"types": types, "categorie": categories})
    return render(request, "modifier.html", {"types": types, "categorie": categories})
def modifier_admin(request, admin_id=None):
    if request.method == 'POST':
        if admin_id is not None:
            admin_cible = User.objects.get(id=admin_id)
            admin_cible.username = request.POST.get("username")
            admin_cible.first_name = request.POST.get("firstname")
            admin_cible.last_name = request.POST.get("lastname")
            admin_cible.email = request.POST.get("email")
            admin_cible.save()
            messages.success(request, "l'administrateur a été modifié")
            return render(request, "modifier_admin.html")
    return render(request, "modifier_admin.html")
def delete_admin(request, admin_id=None):
    admin = User.objects.all()
    ets = Etablissement.objects.all()
    suggestion = Suggestion.objects.all()
    context = {"admin": admin, "ets": ets, "suggestion": suggestion}
    if admin_id is not None:
        user_cible = User.objects.get(id=admin_id)
        user_cible.delete()
        return render(request, "administrate.html", context)
    return render(request, "administrate.html", context)
def delete_suggestion(request, sug_id=None):
    admin = User.objects.all()
    ets = Etablissement.objects.all()
    suggestion = Suggestion.objects.all()
    context = {"admin": admin, "ets": ets, "suggestion": suggestion}
    if sug_id is not None:
        option_cible = Suggestion.objects.get(id=sug_id)
        option_cible.delete()
        return render(request, "administrate.html", context)
    return render(request, "administrate.html", context)