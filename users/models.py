from django.db import models
from django.contrib.auth.models import AbstractUser



# choices in tuple of tuples form with user-readable values
HOUSES = (('A','Aravali'), ('S','Shivalik'), ('N','Nilgiri'), ('U','Udaygiri'))
GENDER = (('F', 'Female'), ('M', 'Male'))


# Create your models here.
class School(models.Model):
    village = models.CharField(blank=False, null=False, max_length=50) # blank used in form validation
    district = models.CharField(blank=False, null=False, max_length=50) # null used in database table constraint
    state = models.CharField(blank=False, null=False, max_length=50)
    pin_code = models.CharField(blank=True, null=True, max_length=6)


class User(AbstractUser):
    mobile_number = models.CharField(blank=True, null=True, unique=True, max_length=10)
    dob = models.DateField(blank=False, null=True)   # required but no default
    gender = models.CharField(blank=False, null=True, choices=GENDER, max_length=1)  # required but no default
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null=True)
    house = models.CharField(choices=HOUSES, max_length=10, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)  # used to add non editable creation date, will cause problem during makemigrations, select option 1
    last_modified = models.DateTimeField(auto_now=True)  # used to update modification date

    # USERNAME_FIELD = 'username'


