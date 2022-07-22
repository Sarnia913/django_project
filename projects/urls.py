from django.urls import path
from .views import project,projects

urlpatterns=[

    path('products/',projects,name='projects'),
    path('project/<str:pk>/',project,name='project')
      ]