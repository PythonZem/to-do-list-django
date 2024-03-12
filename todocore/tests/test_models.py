from django.test import TestCase

from todocore.models import Tag, Task


class TagModelTest(TestCase):
    def test_str_method(self):
        position = Tag.objects.create(name="Test")
        self.assertEqual(str(position), "Test")


class TaskModelTest(TestCase):
    def test_str_method(self):
        task_type = Task.objects.create(content="Some test content")
        self.assertEqual(str(task_type), "Some test content")
