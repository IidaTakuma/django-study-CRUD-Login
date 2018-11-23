from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
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

# class CreateTaskView(CreateView):
#     model = task
#     template_name = 'todo/create.html'
#     success_url = "/"
