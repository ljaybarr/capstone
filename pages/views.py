from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import Contact
from django.core.mail import send_mail

# Create your views here.
class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"
    
def contact(request):
    if request.method == "POST":
        form = Contact(request.POST)
        
        if form.is_valid():
            # get values
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            
            send_mail(
                "Email from " + name,       # subject
                message,                    # content
                email,                      # from
                ["mr.barr900@gmail.com"]    # to
            )
        
    else:
        form = Contact()
    
    return render(request, "pages/contact.html", {"form" : form})