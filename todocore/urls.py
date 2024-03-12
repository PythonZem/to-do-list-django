from django.urls import path

from todocore.views import (
    TagListView,
    TaskCreateView,
    task_make_is_done,
    task_make_is_not_dane,
    TaskUpdateView,
    TagCreateView,
    TagUpdateView,
    TaskDeleteView,
    TaskListView,
    TagDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/is_done/", task_make_is_done, name="task-is-done"),
    path("task/<int:pk>/is_not_done/", task_make_is_not_dane, name="task-is-not-done"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tags-list"),
    path("tags/create/", TagCreateView.as_view(), name="tags-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tags-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tags-delete"),
]