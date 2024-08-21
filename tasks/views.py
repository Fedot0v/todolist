from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from tasks.forms import TaskForm
from tasks.models import Tag, Task


class TagViewList(ListView):
    model = Tag
    template_name = "tasks/tags_list.html"
    context_object_name = "tags"


class TagCreateView(CreateView):
    model = Tag
    fields = "__all__"
    template_name = "tasks/tag_form.html"
    context_object_name = "tag"
    success_url = reverse_lazy("tasks:tags-list")


class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "tasks/tag_form.html"
    context_object_name = "tag"
    success_url = reverse_lazy("tasks:tags-list")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "tasks/tag_confirm_delete.html"
    success_url = reverse_lazy("tasks:tags-list")


class TaskViewList(ListView):
    model = Task
    template_name = "tasks/index.html"
    context_object_name = "tasks"
    ordering = ["is_complete", "created_at"]
    paginate_by = 5

    def post(self, request, *args, **kwargs):
        task_id = request.POST.get("task_id")
        status = request.POST.get("status")

        if task_id is not None and status is not None:
            task = get_object_or_404(Task, pk=task_id)
            task.is_complete = status == "True"
            task.save()

        return redirect("tasks:index")


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/tasks_form.html"
    success_url = reverse_lazy("tasks:index")
    context_object_name = "task"


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/tasks_form.html"
    context_object_name = "task"


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:index")
