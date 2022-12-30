from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views import View
from .forms import RegisterForm

# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'users/home.html')

class RegisterView(View):
    form_class = RegisterForm
    template_name = 'users/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'register_form': form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration Successful')
            return redirect("users:home")
        messages.error(request, 'Unsuccessful registration, Invalid Information')

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "users/login.html",{'login_form':form})
    
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You're now logged in as {username}.")
                return redirect('users:home')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request, "Invalid username or password.")
        return render(request, "users/login.html", {'login_form':form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "You've successfully logged out.")
        return redirect('users:home')



    