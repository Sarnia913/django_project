
from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
# Create your views here.

def projects(request):
    projects=Project.objects.all()
    context={'projects':projects}
    return render(request, './projects/projects.html',context)
def project(request,pk):
    projectobj=Project.objects.get(id=pk)

    context={'num':pk,'projectobj':projectobj}
    return render(request, './projects/single-project.html',context)
def create_project(request):
    form=ProjectForm()
    context={'form':form}
    return render(request,'./projects/project_form.html',context)