from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL

# Create your models here.

# 카테고리 제목 
class Category(models.Model):
    title = models.CharField(max_length=30)


class UserPro(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='user_pro', null=True, blank=True)
    name = models.CharField(max_length=64)
    city = models.TextField()
    age = models.IntegerField()

    def __str__(self):
        return self.name

# 작성글 카테고리 작성자 제목 내용 
class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='contents')
    writer = models.ForeignKey(UserPro, on_delete=models.SET_NULL, related_name='my_contents', null=True, blank=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    is_deleted = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.title

# 댓글 작성글 작성자 내용    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    writer = models.ForeignKey(UserPro, on_delete=models.SET_NULL, related_name='my_comments', null=True, blank=True)
    content = models.TextField()

# 좋아요 유저 작성글    
class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, related_name='like', null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.SET_NULL, related_name='like', null=True, blank=True)
    user = models.ForeignKey(UserPro, on_delete=models.SET_NULL, related_name='like', null=True, blank=True)
