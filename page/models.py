from django.db import models

#on crée une table dans la base de données
class Categorie(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Cycle(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Etablissement(models.Model):
    name = models.CharField(max_length=100, unique=True)
    langue = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    categorie = models.ForeignKey(Categorie, on_delete=models.DO_NOTHING)
    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Etablissement"
        verbose_name_plural = "Etablissements"

class Composer(models.Model):
    etablissement = models.ForeignKey(Etablissement, on_delete=models.DO_NOTHING)
    cycle = models.ForeignKey(Cycle, on_delete=models.DO_NOTHING)

class Suggestion(models.Model):
    titre = models.CharField(max_length=50)
    contenu = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Suggestion"
        verbose_name_plural = "Suggestions"
