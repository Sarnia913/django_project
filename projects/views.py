
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def projects(request):
    return HttpResponse('here are our products.')
def project(request,pk):
    return HttpResponse('one of my project'+pk)