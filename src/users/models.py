from django.contrib.auth.models import AbstractUser
from rest_framework import models

HOUSES = ("Aravali", "Shivalik", "Nilgiri", "Udaygiri")


# Create your models here.
class User(AbstractUser):
    pass

    # first_name = models.CharField(blank=False, null=False)
    # last_name = models.CharField(blank=False, null=False)
    # email_id = models.EmailField(blank=False, null=False, unique=True)
    # mobile_number = models.CharField(blank=True, null=True)
    # age = models.IntegerField(blank=False, null=False)
    # house = models.CharField(choices=HOUSES)
