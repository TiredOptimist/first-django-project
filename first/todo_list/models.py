from django.db import models


class ToDoItem(models.Model):

    class Meta:
        ordering = ("id",)
        verbose_name = "ToDo Item"
    title = models.CharField(max_length=25)
    done = models.BooleanField(default=False)
    description = models.CharField(max_length=250, default="")

    def __str__(self):
        return self.title
