from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=15)
    birth_date = models.CharField(max_length=10)


class BankData(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='bank_data')
    agencia = models.CharField(max_length=155)
    conta = models.CharField(max_length=155)
    digito = models.CharField(max_length=2)


class Enterprise(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='company')
    name = models.CharField(max_length=155)


