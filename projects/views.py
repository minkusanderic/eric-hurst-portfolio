from django.shortcuts import render

from django.http import HttpResponse

from projects.models import Project 

def index(request):
    return render(request, 'projects/list.html')

# Create your views here.
