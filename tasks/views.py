from django.shortcuts import render
from django.views.generic import ListView, CreateView

from tasks.models import Tag, Task


def index(request):
    return render(request, "tasks/index.html")


class TagViewList(ListView):
    model = Tag
    template_name = "tasks/tags_list.html"
    context_object_name = "tags"


class TagCreateView(CreateView):
    model = Tag
    template_name = "tasks/tag_form.html"
    context_object_name = "tag"
    success_url = "tasks:tags-list"


class TaskViewList(ListView):
    model = Task
    template_name = "tasks/index.html"
    context_object_name = "tasks"
    ordering = ["is_complete", "created_at"]
    paginate_by = 5
