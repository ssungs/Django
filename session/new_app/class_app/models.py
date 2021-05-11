from django.db import models
import time

# Create your models here.

class MyClass(models.Model):
    class_num = models.IntegerField()
    Teacher = models.CharField(max_length=30)
    class_room = models.CharField(max_length=30)
    students_num = models.IntegerField()
    is_deleted = models.BooleadField(default=False)
    created_at = models.TextField(default=time.time())
    updated_at = models.TextField(default=time.time())
    # default_created_at = models.DataTimeField()

    def __str__(self):
      return str(self.class_num)

class MyStudents(models.Model):
    class_num = models.ForeignKey(MyClass, on_delete=models.CASCADE, related_name='student')
    is_deleted = models.BooleadField(default=False)
    created_at = models.TextField(default=time.time())
    updated_at = models.TextField(default=time.time())
    name = models.CharField(max_length=30)
    phone_num = models.CharField(max_length=30)
    intro_text = models.TextField()

    def __str__(self):
      return self.name