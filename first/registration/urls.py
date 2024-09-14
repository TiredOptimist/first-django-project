from django.contrib import admin
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, include, reverse_lazy
from django.views.generic import TemplateView
from . import views

app_name = "registration"

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', views.profile_view, name="profile"),
    path('information/', views.information_view, name="information"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('password/', views.UserPasswordChange.as_view(), name="password"),
    path('password_success/', TemplateView.as_view(template_name="registration/password_success.html"), name="password_success"),
    path('update/', views.user_update_view, name="update"),
    path('tems/', TemplateView.as_view(template_name="registration/tems.html"), name="tems"),
    path('reset_form/', PasswordResetView.as_view(
        template_name="registration/reset_form.html",
        email_template_name="registration/reset_email.html",
        success_url=reverse_lazy("registration:reset_done_form")
    ),
         name="reset_form"),
    path('reset_done_form/', PasswordResetDoneView.as_view(template_name="registration/reset_done_form.html"), name="reset_done_form"),
    path('reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name="registration/reset_confirm.html",
        success_url=reverse_lazy("registration:reset_complite"),
    ),
         name="reset_confirm"),
    path('reset_complete/', PasswordResetCompleteView.as_view(template_name="registration/reset_complete.html"), name="reset_complite"),


]