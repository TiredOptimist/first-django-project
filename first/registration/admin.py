from django.contrib import admin
from registration.models import NewUser


@admin.register(NewUser)
class NewUserAdmin(admin.ModelAdmin):
    list_display = "id", "username", "password"
    list_display_links = "username",
