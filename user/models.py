from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomerUser(AbstractUser):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        )
    email = models.EmailField(unique=True,blank=False)
    name = models.CharField(max_length=20,blank=True)
    nickname = models.CharField(max_length=20,blank=True,unique=False)
    gender = models.CharField(max_length=10,blank=True,choices=GENDER_CHOICES)
    birth_date = models.DateField(null=True, blank=False)