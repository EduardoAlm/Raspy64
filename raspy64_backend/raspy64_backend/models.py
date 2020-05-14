from django.db import models


class Users(models.Model):
    Nome = models.CharField(primary_key=False, max_length=150)
    Raspadinha = models.IntegerField(primary_key=False)
    Email = models.CharField(primary_key=False, max_length=150)
    Telemovel = models.IntegerField(primary_key=False)
