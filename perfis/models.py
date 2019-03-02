from django.db import models

class Perfil(models.Model):

    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=50, null=False)
    phone = models.CharField(max_length=15, null=False)
    enterprise = models.CharField(max_length=100, null=False)
