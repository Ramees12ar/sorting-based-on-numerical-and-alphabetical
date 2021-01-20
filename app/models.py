from django.db import models

# Create your models here.
class alphabet(models.Model):
    lid=models.IntegerField(primary_key=True)
    data=models.CharField(max_length=30)
class numeric(models.Model):
    lid=models.IntegerField(primary_key=True)
    data=models.CharField(max_length=30)
class alpha_numer(models.Model):
    lid=models.IntegerField(primary_key=True)
    data=models.CharField(max_length=30)