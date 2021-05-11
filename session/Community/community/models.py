from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateField()
    lists = models.IntegerField()

    def __str__(self):
        return self.title 

class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='contents')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='my_contents', null=True, blank=True)
    title = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    content = models.TextField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class UserPro(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='user', null=True, blank=True)
    user_pro = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='user_pro', null=True, blank=True)
    name = models.CharField(max_length=64)
    city = models.TextField()
    age = models.IntegerField()
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='my_comment', null=True, blank=True)
    comment = models.TextField()

    
