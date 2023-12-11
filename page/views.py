from django.shortcuts import render, redirect
from .models import *
import folium
from django.contrib import messages

# Create your views here.

def home(request):
    stations = Etablissement.objects.all()

    if request.method == 'GET':
        requete = request.GET.get('recherche')
        if requete is not None:
            station = Etablissement.objects.all().filter(name__icontains=requete)
            return render(request, 'requete.html', { 'ets' : station})

    #créer une carte folium centrée sur Ngaoundéré
    m = folium.Map(location=[7.338149, 13.566830], zoom_start=11)

    #ajouter un marqueur sur la carte pour chaque station
    for station in stations:
        coordinates = (station.latitude, station.longitude)
        folium.Marker(coordinates,
                      popup=f"{station.name} <br> {coordinates} <br> {station.langue} <br> {station.categorie} ",
                      tooltip=station.name
                      ).add_to(m)

    context = {"map": m._repr_html_(), "db": stations }
    return render(request, "home.html", context)

def suggestion(request):
    recupere = Suggestion.objects.all()
    if request.method == "POST":
        #recuperation des informations issues du formulaire
        titre = request.POST.get("titre")
        contenu = request.POST.get("contenu")
        new = Suggestion.objects.create(titre=titre, contenu=contenu)
        new.save()
        messages.success(request, "La suggestion a été envoyée avec succés")
        redirect('suggestion')
    return render(request, "suggestion.html", {"ms": recupere})