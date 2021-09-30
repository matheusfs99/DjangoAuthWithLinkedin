from django.contrib.auth.models import User
from django.db import models

# Create your models here.

GENDER = (('M', 'Male'), ('F', 'Female'), ('O', 'Others'))

class Person(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    gender = models.CharField('Gênero', max_length=1, choices=GENDER)
    cpf = models.CharField('CPF', max_length=20, unique=True)
    phone = models.IntegerField('Telefone')
