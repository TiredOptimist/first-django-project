from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

app_name = "todo_list"

urlpatterns = [
   path(
       "",
       views.index_view,
       name="index"
   ),

]
