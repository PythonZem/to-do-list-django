from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView
)

from todocore.forms import TaskForm
from todocore.models import Task, Tag


class TaskListView(ListView):
    model = Task
    ordering = ["is_done", "-datetime"]
    paginate_by = 8
    template_name = "todocore/index.html"


# def task_make_is_done(request, pk):
#     task = Task.objects.get(id=pk)
#     task.is_done = True
#     task.save()
#     return HttpResponseRedirect(reverse_lazy(viewname="index"))
#
#
# def task_make_is_not_dane(request, pk):
#     task = Task.objects.get(id=pk)
#     task.is_done = False
#     task.save()
#     return HttpResponseRedirect(reverse_lazy(viewname="index"))

def task_change_status(request, pk):
    task = Task.objects.get(id=pk)
    task.is_done = not task.is_done
    task.save()
    return HttpResponseRedirect(reverse_lazy(viewname="index"))


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("index")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("index")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("index")


class TagCreateView(CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tags-list")


class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tags-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("tags-list")


class TagListView(ListView):
    model = Tag
    paginate_by = 8
