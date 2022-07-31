
from django.shortcuts import render,redirect
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
    if request.method == 'POST':
       form=ProjectForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('projects')
    form = ProjectForm()
    context = {'form': form}
    return render(request, './projects/project_form.html', context)