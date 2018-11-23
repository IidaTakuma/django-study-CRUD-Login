from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView,CreateView
from .models import Task
# Create your views here.
class IndexView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todo/index.html'

    def get_queryset(self):
        return Task.objects.filter(is_done=False).order_by('created_at')

class DetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/detail.html'

class EditView(UpdateView):
    model = Task
    context_object_name = 'task'
    fields = ("title","description",)
    template_name = 'todo/edit.html'
    success_url = "/"

class CreateView(CreateView):
    model = Task
    fields = ("title","description","created_by",)
    template_name = 'todo/create.html'
    success_url = "/"
