from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib import messages


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
        user = User.objects.create_user(username=username, email=email ,password=password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        messages.success(request, "Le compte a été crée avec succès")
        return redirect("login")
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
    return render(request, "administrate.html")