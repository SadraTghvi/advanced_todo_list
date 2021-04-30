from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import *
from django.urls import reverse_lazy

from django.contrib.auth.views import *

from .models import Task

# Create your views here.

class CustomLoginView(LoginView):
    template_name = "todo_list/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("tasks")
    
class TaskList(ListView):
    model = Task
    context_object_name = "tasks"

class TaskDetail(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "todo_list/task.html"

class TaskCreate(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")

class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")

class TaskDelete(DeleteView):
    model = Task
    template_name = "todo_list/task_delete.html"
    context_object_name = "task"
    success_url = reverse_lazy("tasks")
