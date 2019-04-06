from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserInfo(AbstractUser):
    # 扩展auth模块默认的数据表
    phone = models.CharField(max_length=11)
