from __future__ import unicode_literals

from django.db import models


class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    gender = models.BooleanField(default=1)
    age = models.IntegerField(default=19)
    memo = models.TextField(default = "xxx")
    createdate = models.DateTimeField(auto_now=True)
    typeid = models.ForeignKey("UserType",default=1)


class UserType(models.Model):
    name = models.CharField(max_length=50)


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50,null=True)
    group_relation = models.ManyToManyField("Group")


class Group(models.Model):
    groupname = models.CharField(max_length=50)


class UploadFile(models.Model):
    userid = models.CharField(max_length=50)
    file = models.FileField(upload_to='./upload/')
    data = models.DateTimeField(auto_now_add=True)
# Create your models here.
