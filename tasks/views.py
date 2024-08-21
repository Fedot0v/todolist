from django.shortcuts import render
from django.views.generic import ListView

from tasks.models import Tag, Task


def index(request):
    return render(request, "tasks/index.html")


class TagViewList(ListView):
    model = Tag
    template_name = "tasks/tags_list.html"
    context_object_name = "tags"


class TaskViewList(ListView):
    model = Task
    template_name = "tasks/tasks_list.html"
    context_object_name = "tasks"
    ordering = ["is_complete", "created_at"]
