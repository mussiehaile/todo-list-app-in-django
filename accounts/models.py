from django.db import models

# Create your models here.


class Account(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    # Add more fields as per your requirements

    def __str__(self):
        return self.username

