from django.db import models
from django.contrib.auth.models import AbstractUser


class NewUser(AbstractUser):
    class Meta:
        ordering = ("username",)
        verbose_name = "User"
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=254, default='')
    status = models.CharField(max_length=250, blank=True, default='')
    avatar = models.ImageField(upload_to='uploads/static/img', height_field=None, width_field=None, max_length=100,
        blank =True, default='static/img/default.jpg')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username


