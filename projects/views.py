from django.shortcuts import render

from django.http import HttpResponse

from projects.models import Project 

def index(request):
    all_projects = Project.objects.all() 
    context = { 'projects' : all_projects } 
    return render(request, 'projects/list.html', context)

# Create your views here.
