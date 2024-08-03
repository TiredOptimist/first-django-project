from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView, View
from .forms import ToDoItemForm
from .models import ToDoItem


def index_view(request: HttpRequest) -> HttpResponse:
    todo_item = ToDoItem.objects.order_by("id").all()
    # todo_item = ["Item1", "Item2",]
    return render(request, template_name="todo_list/index.html", context={"todo_items": todo_item[:2]},)



class ToDoListIndexView(ListView):
    template_name = "todo_list/index.html"
    model = ToDoItem
    queryset = ToDoItem.objects.order_by("-id").all()[:5]


class ToDoListDoneView(ListView):
   queryset = ToDoItem.objects.filter(done=False).all()


class ToDoListView(ListView):
    model = ToDoItem


class ToDoDetailView(DetailView):
    model = ToDoItem


class AddTodoItem(View):
    template_name = 'todo_list/add_todo_item.html'

    def get(self, request):
        form = ToDoItemForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ToDoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list:index')
        return render(request, self.template_name, {'form': form})


class DeleteTodoView(View):
    template_name = 'todo_list/delete_todo.html'

    def post(self, request, todo_id):
        todo_item = get_object_or_404(ToDoItem, pk=todo_id)
        todo_item.delete()
        return redirect('todo_list:index')

    def get(self, request, todo_id):
        todo_item = get_object_or_404(ToDoItem, pk=todo_id)
        return render(request, self.template_name, {'todo_item': todo_item})


class ToggleDoneView(View):

    def post(self, request, pk):
        todo_item = ToDoItem.objects.get(pk=pk)
        todo_item.done = True
        todo_item.save()
        return redirect(request.META.get('HTTP_REFERER'))
