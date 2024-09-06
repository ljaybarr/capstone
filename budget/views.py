from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Project, Category, Expense
from django.views.generic import CreateView, UpdateView, DeleteView
from django.utils.text import slugify
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ExpenseForm
import json

# Create your views here.
def project_list(request):
    project_list = Project.objects.filter(author=request.user)
    return render(request, 'budget/project-list.html', {'project_list': project_list})

def project_detail(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    
    if request.method == 'GET':
        category_list = Category.objects.filter(project=project)
        expenses = project.expenses.all()    
        return render(request, 'budget/project-detail.html', {'project': project, 'expense_list': expenses, 'category_list': category_list })

    elif request.method == 'POST':
        # process the form
        form = ExpenseForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            amount = form.cleaned_data['amount']
            category_name = form.cleaned_data['category']
            
            category = get_object_or_404(Category, project=project, name=category_name)
            
            Expense.objects.create(
                project=project,
                title=title,
                amount=amount,
                category=category
            ).save()
            
    elif request.method == 'DELETE':
        id = json.loads(request.body)['id']
        expense = get_object_or_404(Expense, id=id)
        expense.delete()
        
        return HttpResponse('')
    
    return HttpResponseRedirect(project_slug)

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'budget/add-project.html'
    fields = ('name', 'budget')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        self.object = form.save(commit=False)
        self.object.save()
        
        categories = self.request.POST['categoriesString'].split(',')
        for category in categories:
            Category.objects.create(
                project=Project.objects.get(id=self.object.id),
                name=category
            ).save()
            
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return slugify(self.request.POST['name'])
    
class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'budget/add-project.html'
    fields = ('name', 'budget')
    slug_field = 'slug'
    slug_url_kwarg ='project_slug'
    
    def form_valid(self, form):
        project = self.object
        form.instance.author = self.request.user
        self.object = form.save(commit=False)
        self.object.save()
    
        categories = self.request.POST['categoriesString'].split(',')
        for category in categories:
            Category.objects.create(
                project=Project.objects.get(id=self.object.id),
                name=category
            ).save()
        
        return super().form_valid(form)

    def get_success_url(self):
        project = self.object
        return reverse('detail', kwargs={"project_slug":project.slug})
      
def project_delete(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    project.delete()
    return redirect('list')
    