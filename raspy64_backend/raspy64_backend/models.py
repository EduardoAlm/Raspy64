from django.db import models


class Users(models.Model):
    Raspadinha = models.IntegerField(primary_key=False)
    Telemovel = models.IntegerField(primary_key=False)
