from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView,UpdateView,CreateView
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import TaskForm
# Create your views here.
@method_decorator(login_required, name='dispatch')
class IndexView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todo/index.html'

    def get_queryset(self):
        return Task.objects.filter(is_done=False,created_by=self.request.user).order_by('created_at')

@method_decorator(login_required, name='dispatch')
class DetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/detail.html'

@method_decorator(login_required, name='dispatch')
class EditView(UpdateView):
    model = Task
    form_class = TaskForm
    context_object_name = 'task'
    template_name = 'todo/edit.html'
    success_url = "/"

@method_decorator(login_required, name='dispatch')
class CreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/create.html'
    success_url = "/"

    def form_valid(self,form):
        post = form.save(commit=False)
        post.created_by = self.request.user
        post.save()
        return redirect('todo:index')
