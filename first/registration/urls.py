from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

app_name = "registration"

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', views.profile_view, name="profile"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('password/', views.change_password, name="password")

]
