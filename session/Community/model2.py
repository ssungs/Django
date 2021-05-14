from django.db import models
from django.contrib.auth.models import User
import time

from django.db.models.deletion import SET_NULL

class UserPro(models.Model):
    user_pro = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='user_pro', null=True, blank=True)
    name = models.CharField(max_length=64)


class Content(models.Model):
    writer = models.ForeignKey(UserPro, on_delete=models.SET_NULL, related_name='content_writer', null=True, blank=True)
    content = models.TextField()
    create_at = models.TextField(default=time.time())


class Comment(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='comment')
    writer = models.ForeignKey(UserPro, on_delete=models.CASCADE, related_name='comment')
    content = models.TextField()
    create_at = models.TextField(default=time.time())

    
class Like(models.Model):
    content = models.ForeignKey(Comment, on_delete=models.SET_NULL, related_name='like', null=True, blank=True)
    user = models.ManyToManyField(UserPro, on_delete=models.SET_NULL, related_name='like', null=True, blank=True)
    # user = models.ForeignKey(UserPro, on_delete=models.SET_NULL, related_name='like', null=True, blank=True)
    # comment = models.OneToOneField(Comment, on_delete=models.CASCDE, related_name='liked_comment')








# 쇼핑몰 서비스 고객 구매 물품 회원등급

# 등급 : 등급명 할인률
class Grade(models.Model):
    grade = models.CharField(max_length=64) 
    discount = models.IntegerField()

# 상품 이름 가격
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

# 유저 이름 등급
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    name = models.CharField(max_length=64)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='grade')

# 유저 구매한 물품
class Basket(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='basket')
    user = models.ForeignKey(UserPro, on_delete=models.CASCADE, related_name='user_basket')

class TotalPrice(models.Model):
    user = 







# 미용실

# 상품 이름 가격
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

# 유저 이름 예약내역 예약상품
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='userprofile', null=True, blank=True)
    name = models.CharField(max_length=64)
    is_reservation = models.BooleanField(default=False)
    # product = models.ForeignKey(Product, on_delete=SET_NULL, related_name='user_product', null=True, blank=True)

# 예약 날짜 시간 결제상태 방문확인 환불상태
class Reservation(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, related_name='userprofile' ,null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name='reservation', null=True, blank=True)
    date = models.IntegerField()
    time = models.IntegerField()
    is_payment = models.BooleanField(default=False)
    is_visit = models.BooleanField(default=False)
    is_refund = models.BooleanField(default=False)


# views.py
