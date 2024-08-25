from django.db import models

# Create your models here.
class User(models.Model):
    nom = models.CharField(max_length=70)
    prenom = models.CharField(max_length=70)
    age = models.CharField(max_length=4)
    email = models.CharField(max_length=100)
    option = models.CharField(max_length=50)
    