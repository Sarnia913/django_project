from django.urls import path
from .views import project,projects,create_project

urlpatterns=[

    path('',projects,name='projects'),
    path('what/<str:pk>/',project,name='project'),
    path('create_project_form/', create_project, name='create_project')
      ]