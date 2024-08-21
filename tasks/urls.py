from django.urls import path

from tasks import views
from tasks.views import (
    TaskViewList,
    TagViewList,
    TagCreateView, TagUpdateView
)

app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("tasks", TaskViewList.as_view(), name="tasks-list"),
    path("tags", TagViewList.as_view(), name="tags-list"),
    path("tags/create/", TagCreateView.as_view(), name="tags-form"),
    path("tags/<int:pk>/create/", TagUpdateView.as_view(), name="tags-form"),
]