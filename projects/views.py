
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
projectslist=[
    {'id':1,
      'title':'ecommerce website',
     'desc':'fully functional ecommerce website'},
    {'id':2,
      'title':'portfolio website',
     'desc':'my portfolio'},
    {'id':3,
      'title':'social network',
     'desc':'a sample network'}
]
def projects(request):
    page='projects'
    number=12
    context={'page':page,'number':number,'projects':projectslist}
    return render(request, './projects/projects.html',context)
def project(request,pk):
    projectobj=None
    for proj in projectslist:
        if proj['id']==int(pk):
            projectobj=proj
    context={'num':pk,'project':projectobj}
    return render(request, './projects/single-project.html',context)