from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView
from .forms import ToDoItemForm
from .models import ToDoItem


def index_view(request: HttpRequest) -> HttpResponse:
    todo_item = ToDoItem.objects.order_by("id").all()
    # todo_item = ["Item1", "Item2",]
    return render(request, template_name="todo_list/index.html", context={"todo_items": todo_item[:2]},)


class ToDoListIndexView(ListView):
    template_name = "todo_list/index.html"
    model = ToDoItem
    queryset = ToDoItem.objects.order_by("-id").all()[:3]


class ToDoListDoneView(ListView):
   queryset = ToDoItem.objects.filter(done=False).all()


class ToDoListView(ListView):
    model = ToDoItem


class ToDoDetailView(DetailView):
    model = ToDoItem


def add_todo_item(request):
    if request.method == 'POST':
        form = ToDoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = ToDoItemForm()
    return render(request, 'add_todo_item.html', {'form': form})