from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

app_name = "todo_list"

urlpatterns = [
    # path( "", views.index_view, name="index"),
    # path("", views.ToDoListIndexView.as_view(), name="index")
    path("", views.ToDoListIndexView.as_view(), name="index"),
    path("list/", views.ToDoListView.as_view(), name="list"),
    path("done/", views.ToDoListDoneView.as_view(), name="done"),
    path("true_done/", views.ToDoListTrueDoneView.as_view(), name="true_done"),
    path("<int:pk>/", views.ToDoDetailView.as_view(), name="detail"),
    path('add_todo_item/', views.AddTodoItem.as_view(), name='add_todo_item'),
    path('delete_todo/<int:todo_id>/', views.DeleteTodoView.as_view(), name='delete_todo'),
    path('todo/<int:pk>/toggle_done/', views.ToggleDoneView.as_view(), name='toggle_done'),
]
