from django.shortcuts import render, redirect
from .models import *
import folium
from django.contrib import messages

# Create your views here.

def home(request, ecole_id=None):
    stations = Etablissement.objects.all()

    if request.method == 'GET':
        requete = request.GET.get('recherche')
        filtre = request.GET.get('filtre')
        if requete is not None:
            requete = str(requete)
            if requete != '':
                filtre = str(filtre)
                station = Etablissement.objects.all()
                if filtre == 'nom':
                    station = Etablissement.objects.all().filter(name__icontains=requete)
                elif filtre == 'langue':
                    station = Etablissement.objects.all().filter(langue__icontains=requete)
                elif filtre == 'type':
                    genres = Type.objects.all().filter(name__icontains=requete)
                    if genres.count() > 0:
                        for gen in genres:
                            station = Etablissement.objects.all().filter(type__exact=gen.id)
                    else :
                        station = None
                else:
                    categories = Categorie.objects.all().filter(name__icontains=requete)
                    if categories.count() > 0:
                        for cate in categories:
                            station = Etablissement.objects.all().filter(categorie__exact=cate.id)
                    else :
                        station = None

                return render(request, 'requete.html', {'ets': station})
    #créer une carte folium centrée sur Ngaoundéré
    m = folium.Map(location=[7.338149, 13.566830], zoom_start=11)

    #ajouter un marqueur sur la carte pour chaque station
    for station in stations:
        coordinates = (station.latitude, station.longitude)
        folium.Marker(coordinates,
                      popup=f"{station.name} <br> {coordinates} <br> {station.langue} <br> {station.categorie} ",
                      tooltip=station.name
                      ).add_to(m)
        if ecole_id is not None and station.id == ecole_id:
            coordinates = (station.latitude, station.longitude)
            folium.Marker(coordinates,
                          popup=f"{station.name} <br> {coordinates} <br> {station.langue} <br> {station.categorie} ",
                          tooltip=station.name,
                          icon=folium.Icon(color="red"),
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
        return redirect('suggestion')
    return render(request, "suggestion.html", {"ms": recupere})
def apropos(request):
    return render(request, "apropos.html")