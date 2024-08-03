from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.auth import logout
from django.urls import reverse
from django.shortcuts import redirect
from .forms import UserRegisterForm

# Create your views here.
class UserLoginView(LoginView):
    template_name = "users/login.html"
    
    def get_success_url(self):
        return reverse('home')


class UserRegisterView(CreateView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    
    def form_valid(self, form):
        user = form.save(commit=False)
        passw = form.cleaned_data["password"]
        user.set_password(passw) # hash/encrypt the password
        
        user.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('login')
    
    

def user_logout_view(request):
    logout(request)
    return redirect('login')