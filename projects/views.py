
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
def update_project(request,pk):
    project=Project.objects.get(id=pk)
    if request.method=='POST':
        form=ProjectForm(request.POST,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    form = ProjectForm(instance=project)
    context = {'form': form}
    return render(request, './projects/project_form.html', context)
def delete_project(request,pk):
    if request.method=='POST':
        project=Project.objects.filter(id=pk).delete()
        return redirect('projects')
    project=Project.objects.get(id=pk)
    context = {'object': project}
    return render(request, './projects/delete_template.html', context)