from django.db import models
from django.contrib.auth.models import AbstractUser


class NewUser(AbstractUser):
    class Meta:
        ordering = ("username",)
        verbose_name = "User"
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=254, default='')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username


