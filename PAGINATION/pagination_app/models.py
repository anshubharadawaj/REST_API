# Create your models here.
from django.db import models

#Code for signals file we can also write here
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    roll=models.IntegerField()
