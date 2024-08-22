from django.contrib import admin
from django.urls import path, include
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

]
