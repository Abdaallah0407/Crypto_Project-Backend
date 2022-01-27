import email
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=20, blank=True)
    email = models.EmailField(verbose_name="Элекронная почта", max_length=50, blank=True)
    company = models.CharField(verbose_name="Наименование организации", max_length=100, blank=True)
    
    def __str__(self):
        return self.username