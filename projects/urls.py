from django.urls import path
from .views import project,projects,create_project,update_project,delete_project

urlpatterns=[

    path('',projects,name='projects'),
    path('what/<str:pk>/',project,name='project'),
    path('create_project/', create_project, name='create_project'),
    path('update_project/<str:pk>/',update_project,name='update_project'),
    path('delete_project/<str:pk>/',delete_project,name='delete_project')
      ]