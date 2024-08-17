from django.db import models
from registration.models import NewUser


def get_sentinel_user():
    return NewUser.objects.get_or_create(username="deleted")[0]


def get_sentinel_user_id():
    return get_sentinel_user().id


class ToDoItem(models.Model):

    class Meta:
        ordering = ("id",)
        verbose_name = "ToDo Item"
    title = models.CharField(max_length=25)
    done = models.BooleanField(default=False)
    description = models.CharField(max_length=250, default="")
    user = models.ForeignKey(NewUser, on_delete=models.SET(get_sentinel_user), default=get_sentinel_user_id)

    def __str__(self):
        return self.title
