from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    """
    Custom class to modified Django's default user
    """
    birthdate = models.DateField(verbose_name='Fecha de nacimiento', null=True, blank=True)
