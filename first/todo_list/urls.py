from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

app_name = "todo_list"

urlpatterns = [
   path(
       "",
       TemplateView.as_view(
           template_name="todo_list/index.html"),
       name="index"
   ),

]
