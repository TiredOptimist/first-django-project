from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView, View
from .forms import ToDoItemForm
from .models import ToDoItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def index_view(request: HttpRequest) -> HttpResponse:
    todo_item = ToDoItem.objects.filter(user=request.user).order_by("id").all()
    # todo_item = ["Item1", "Item2",]
    return render(request, template_name="todo_list/index.html", context={"todo_items": todo_item[:2]},)


class ToDoListIndexView(LoginRequiredMixin, ListView):
    template_name = "todo_list/index.html"
    model = ToDoItem

    def get_queryset(self):
        return ToDoItem.objects.filter(user=self.request.user).order_by("-id").filter(done=False).all()[:5]


class ToDoListDoneView(LoginRequiredMixin, ListView):

    def get_queryset(self):
        return ToDoItem.objects.filter(user=self.request.user).filter(done=False).all()


class ToDoListTrueDoneView(ListView):
    def get_queryset(self):
        return ToDoItem.objects.filter(user=self.request.user).filter(done=True).all()


class ToDoListView(ListView):
    model = ToDoItem

    def get_queryset(self):
        return ToDoItem.objects.filter(user=self.request.user)


class ToDoDetailView(DetailView):
    model = ToDoItem

    def get_queryset(self):
        return ToDoItem.objects.filter(user=self.request.user)


class AddTodoItem(LoginRequiredMixin, View):
    template_name = 'todo_list/add_todo_item.html'

    def get(self, request):
        form = ToDoItemForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ToDoItemForm(request.POST)
        if form.is_valid():
            todo_item = form.save(commit=False)
            todo_item.user = self.request.user
            todo_item.save()
            return redirect('todo_list:index')
        return render(request, self.template_name, {'form': form})


class DeleteTodoView(LoginRequiredMixin, View):
    template_name = 'todo_list/delete_todo.html'

    def post(self, request, todo_id):
        todo_item = get_object_or_404(ToDoItem, pk=todo_id, user=request.user)
        todo_item.delete()
        return redirect('todo_list:index')

    def get(self, request, todo_id):
        todo_item = get_object_or_404(ToDoItem, pk=todo_id, user=request.user)
        return render(request, self.template_name, {'todo_item': todo_item})


class ToggleDoneView(LoginRequiredMixin, View):

    def post(self, request, pk):
        todo_item = get_object_or_404(ToDoItem, pk=pk, user=request.user)
        todo_item.done = not todo_item.done
        todo_item.save()
        return redirect(request.META.get('HTTP_REFERER'))
