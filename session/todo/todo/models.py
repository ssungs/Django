from django.db import models

# Create your models here.

class TodoList(models.Model):
    todolist = models.CharField(max_length=64)
    is_complete = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)