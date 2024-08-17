from django.db import models
from django.contrib.auth.models import AbstractUser


class NewUser(AbstractUser):
    class Meta:
        ordering = ("username",)
        verbose_name = "User"
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=30, null=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


