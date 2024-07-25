from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import ToDoItem


def index_view(request: HttpRequest) -> HttpResponse:
    todo_item = ToDoItem.objects.order_by("id").all()
    # todo_item = ["Item1", "Item2",]
    return render(request, template_name="todo_list/index.html", context={"todo_items": todo_item},)