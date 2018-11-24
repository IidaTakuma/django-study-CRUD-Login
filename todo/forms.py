from django import forms
from django.db import models
from .models import Task

class TaskForm(forms.ModelForm):

  class Meta:
    model = Task
    fields = ('title', 'description',)
    widgets = {
      'description': forms.Textarea(attrs={'rows':2}),
    }