from django.contrib import admin
from .models import Category, Article, UserPro, Comment, Like


# Register your models here.

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(UserPro)
admin.site.register(Comment)
admin.site.register(Like)