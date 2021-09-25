from django.db import models
from django.conf import settings


# Create your models here.

# 멋사
class Likelion(models.Model) :
    likelion_first = models.CharField(max_length=200, verbose_name= "멋 likelion_first") # default = "멋" 을 넣어야 하나??
    likelion_second = models.CharField(max_length=200, verbose_name= "사 likelion_first") # default = "사" 를 넣어야 하나??
    created = models.DateTimeField(auto_now_add=True, verbose_name = "최근 순 created")
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name = "작성자 writer")
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name ='like_counts', verbose_name="좋아요 수 like_users")


# 어흥
class Growl(models.Model):
    growl_first = models.CharField(max_length=200, verbose_name= "어 growl_first") # default = "어" 를 넣어야 하나??
    growl_second = models.CharField(max_length=200, verbose_name= "흥 growl_first") # default = "흥" 을 넣어야 하나??
    created = models.DateTimeField(auto_now_add=True, verbose_name = "최근 순 created")
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name = "작성자 writer")
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name ='growl_like_counts', verbose_name="좋아요 수 like_users")
