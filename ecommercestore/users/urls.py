from django import views
from django.urls import path
from users.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home')
]

