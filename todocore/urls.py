from django.urls import path

from todocore.views import (
    TagListView,
    TaskCreateView,
    task_make_is_done,
    task_make_is_not_dane,
    TaskUpdateView,
    TagCreateView,
    TagUpdateView,
    tag_delete,
    task_delete,
    TaskListView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/is_done/<int:pk>", task_make_is_done, name="task-is-done"),
    path("task/is_not_done/<int:pk>", task_make_is_not_dane, name="task-is-not-done"),
    path("task/update/<int:pk>", TaskUpdateView.as_view(), name="task-update"),
    path("task/delete/<int:pk>", task_delete, name="task-delete"),
    path("tags/", TagListView.as_view(), name="tags-list"),
    path("tags/create/", TagCreateView.as_view(), name="tags-create"),
    path("tags/update/<int:pk>", TagUpdateView.as_view(), name="tags-update"),
    path("tags/delete/<int:pk>", tag_delete, name="tags-delete"),
]
