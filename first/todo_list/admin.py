from django.contrib import admin

from todo_list.models import ToDoItem


@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = "id", "title", "done", "description", "user", "created_at", "deadline"
    list_display_links = "id", "title"
