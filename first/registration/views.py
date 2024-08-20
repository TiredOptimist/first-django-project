from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'registration:login', {'form': form})


@login_required
def profile_view(request):
    user = request.user
    context = {'username': user.username, 'email': user.email }
    return render(request,"registration/profile.html", context)


@require_http_methods
def logout_view(request):
    logout(request)
    return redirect('registration:login')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('todo_list:index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)



