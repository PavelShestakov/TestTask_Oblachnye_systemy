from django.db import models

# Create your models here.
class Account(models.Model):
    """Модель для хранения данных для авторизации на сайте"""
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.username}"
