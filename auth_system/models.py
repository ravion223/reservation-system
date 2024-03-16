from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    phone_num = models.CharField(max_length = 63, blank=True, null=True)

    def __str__(self):
        return f"User {self.username}"
