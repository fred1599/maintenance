from django.db import models


class Equipement(models.Model):
    nom = models.CharField(max_length=250)

    def emprunter(self):
        nouvel_historique = Historique.objects.create(equipement=self)


class Historique(models.Model):
    equipement = models.ForeignKey(Equipement, on_delete=models.PROTECT)
    date_utilisation = models.DateField(auto_now_add=True)

