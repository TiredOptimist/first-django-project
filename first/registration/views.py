from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from .forms import RegisterForm, UserPasswordChangeForm
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView


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
    context = {'username': user.username, 'email': user.email, 'status': user.status}
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


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("registration:password_success")
    template_name = "registration/password.html"
