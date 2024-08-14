from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.auth import logout
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from .forms import UserRegisterForm
from .models import Profile
from django.views import View
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User

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
        
        # auto create a profile for every user
        Profile.objects.create(user=user)
        
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('login')
    
    

def user_logout_view(request):
    logout(request)
    return redirect('login')




#################################################################
###################### PROFILE VIEWS ############################
#################################################################



class UserProfileEditView(View):
    template_name = "users/edit_profile.html"
    
    def get(self, request):
        return render(request, self.template_name, {'user': request.user})
    
    def post(self, request):
        profile = request.user.profile
        profile.phone_number = request.POST.get('phone_number')
        
        if 'avatar' in request.FILES:
            profile.avatar= request.FILES['avatar']
            
        profile.save()
        return redirect('profile')
    
    
class UserProfileView(DetailView):
    models = User
    template_name = "users/profile.html"
    context_object_name = "user"
    pk_url_kwarg = "user_id"
    
    def get_object(self):
        user_id = self.kwargs.get('user_id')
        return get_object_or_404(User, id=user_id)