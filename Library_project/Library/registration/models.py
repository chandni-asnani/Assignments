from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_num = models.IntegerField(max_length = 10, blank=True, null=True)
    password = models.CharField(max_length = 200, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):
        print(self.name)
        return str(self.name)

