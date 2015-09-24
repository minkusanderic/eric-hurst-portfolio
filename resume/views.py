from django.shortcuts import render

from django.http import HttpResponse

from resume.models import Education

def index(request):
    schools = Education.objects.all()
    context = {'edu': schools}
    return render(request, 'resume/data-science.html', context)

def datascience(request):
    schools = Education.objects.all()
    context = {'edu': schools}
    return render(request, 'resume/data-science.html', context)

def raw_datascience(request):
    schools = Education.objects.all()
    context = {'edu': schools}
    return render(request, 'resume/raw/data-science.html', context)

# Create your views here.
