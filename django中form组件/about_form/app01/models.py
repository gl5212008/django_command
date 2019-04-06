from django.db import models

# Create your models here.


class UserInfo(models.Model):
    name = models.CharField(max_length=16)
    pwd = models.CharField(max_length=32)


class Job(models.Model):
    name = models.CharField(max_length=12)
