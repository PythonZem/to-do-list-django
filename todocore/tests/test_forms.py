from django.test import TestCase
from todocore.forms import TaskForm
from todocore.models import Tag


class TaskFormTest(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name="Work")
        self.tag2 = Tag.objects.create(name="Study")

    def test_task_form_valid(self):
        form_data = {
            "content": "Test Task",
            "deadline_0": "2024-03-11",
            "deadline_1": "12:00",
            "tags": [self.tag1.id, self.tag2.id],
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_form_invalid(self):
        form_data = {
            "deadline_0": "2024-03-11",
            "deadline_1": "12:00",
            "tags": [self.tag1.id, self.tag2.id],
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
