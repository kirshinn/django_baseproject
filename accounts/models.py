from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
