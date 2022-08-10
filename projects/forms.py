from django.forms import ModelForm,widgets
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model=Project
        fields='__all__'
        widgets={
            'tags':forms.CheckboxSelectMultiple(),
        }