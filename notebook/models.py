from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class NoteNames(models.Model):
    userName = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=12)
    dateOfBirth = models.DateField()


class Aux(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)