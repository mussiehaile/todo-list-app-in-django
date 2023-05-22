from django.db import models 
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Account(AbstractUser):
    username = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    age=  models.IntegerField(default=3)
    # Add more fields as per your requirements

    def __str__(self):
        return self.username


# accounts/models.py

from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
# Add your additional fields for the user profile here
    

    def __str__(self):
        return self.user.username


    def __str__(self):
        return self.user.username