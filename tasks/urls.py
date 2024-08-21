from django.urls import path

from tasks import views
from tasks.views import (
    TaskViewList,
    TagViewList,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskCreateView,
    TaskUpdateView, TaskDeleteView
)

app_name = "tasks"

urlpatterns = [
    path("", TaskViewList.as_view(), name="index"),
    path("tags", TagViewList.as_view(), name="tags-list"),
    path("tags/create/", TagCreateView.as_view(), name="tags-create"),
    path(
        "tags/<int:pk>/create/",
        TagUpdateView.as_view(),
        name="tags-update"
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tags-delete"
    ),
    path("task/create", TaskCreateView.as_view(), name="tasks-create"),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="tasks-update"
    ),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="tasks-delete"
    ),

]