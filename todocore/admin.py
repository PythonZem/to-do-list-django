from django.contrib import admin

from todocore.models import Tag, Task

# Register your models here.
admin.site.register(Tag)
admin.site.register(Task)
