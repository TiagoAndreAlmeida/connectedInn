from django.db import models

class Perfil (models.Model):
    name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=15, null=False)
    coorp = models.CharField(max_length=255, null=False)