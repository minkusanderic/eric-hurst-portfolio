from django.shortcuts import render

from django.http import HttpResponse

from resume.models import Education

def index(request):
    schools = Education.objects.all()
    context = {'edu': schools}
    return render(request, 'resume/index.html', context)

# Create your views here.
