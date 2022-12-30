from django import views
from django.urls import path
from users.views import Home
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('login',views.LoginView.as_view(), name='login'),
    path('logout',views.LogoutView.as_view(), name='logout')
]

