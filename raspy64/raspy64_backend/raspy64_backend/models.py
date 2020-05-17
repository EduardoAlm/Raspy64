from django.db import models


class Users(models.Model):
    UID = models.CharField(max_length=150)
    Telemovel = models.CharField(max_length=150)
    Username = models.CharField(max_length=150)
    Raspadinha = models.CharField(max_length=150)
