from django.contrib import admin
from django.urls import path
from .views import project_list, project_detail, project_delete, ProjectUpdateView, ProjectCreateView

urlpatterns = [
    path('', project_list, name="list"),
    path('add', ProjectCreateView.as_view(), name='add'),
    path('<slug:project_slug>', project_detail, name='detail'),
    path('<slug:project_slug>/edit', ProjectUpdateView.as_view(), name='edit'),
    path('<slug:project_slug>/delete', project_delete, name='delete'),
]