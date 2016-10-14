# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Item(models.Model):
    status_choice = (
             (0,'等待'),
             (1,'开始'),
             (2,'完成'),
         )
    del_status_choice = (
             (0,'正常'),
             (1,'删除'),
     )
    name = models.CharField(max_length=50)
    userid = models.IntegerField(max_length=11,blank=True)
    itype = models.CharField(max_length=50)
    adddate = models.DateTimeField(auto_now_add=True)
    startdate = models.DateField(null=True)
    enddate = models.DateField(null=True)
    content = models.TextField(null=True)
    status = models.IntegerField(max_length=4, choices=status_choice,default=0)
    del_userid = models.IntegerField(max_length=11,blank=True)
    del_status = models.IntegerField(max_length=4, choices=del_status_choice,default=0)

    def __unicode__(self):
        return self.name


class User(models.Model):
    sex_choice = (
             (0,'男'),
             (1,'女'),
         )
    access_chioce = (
            (0,'普通'),
            (1,'管理员'),
    )
    status_choice = (
            (0,'正常'),
            (1,'删除'),
    )
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=50)
    passwd = models.CharField(max_length=50)
    phone = models.IntegerField(max_length=11, null=True)
    birthday = models.DateField(null=True)
    sex = models.IntegerField(max_length=4,choices=sex_choice,default=0)
    qq = models.IntegerField(max_length=11,null=True)
    email = models.EmailField(null=True)
    department = models.ForeignKey("Department")
    access = models.IntegerField(max_length=4,choices=access_chioce, default=0)
    image = models.ImageField(max_length=50, null=True)
    adddate =models.DateTimeField(null=True)
    status = models.IntegerField(choices=status_choice,default=0)


class Task(models.Model):
    status_choice = (
        (0, '未接'),
        (1, '开始'),
        (2, '结束'),
    )
    priority_choice = (
        (0, '最低'),
        (1, '普通'),
        (2, '紧急'),
    )
    status_choice = (
            (0,'正常'),
            (1,'删除'),
    )
    inputid = models.IntegerField(max_length=11)
    inputdate = models.DateTimeField(null=True)
    userid = models.IntegerField(max_length=11)
    depid = models.IntegerField(max_length=11)
    assistid = models.IntegerField(max_length=11)
    assdepid = models.IntegerField(max_length=11)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    status = models.IntegerField(choices=status_choice,default=0)
    startdate = models.DateTimeField(auto_now_add=True)
    enddate = models.DateTimeField(auto_now_add=True)
    begindate = models.DateTimeField(null=True)
    finishdate = models.DateTimeField(null=True)
    evaluate = models.TextField(null=True)
    priority = models.IntegerField(max_length=4, choices=priority_choice, default=0)
    itemid = models.IntegerField(max_length=11,null=True)
    departmentid = models.IntegerField(max_length=11)
    del_userid = models.IntegerField(max_length=11,null=True)
    del_status = models.IntegerField(max_length=11,choices=status_choice,default=0)


class Task_reply(models.Model):
    userid = models.IntegerField(max_length=11)
    content = models.TextField()
    editdate = models.DateTimeField()
    taskid = models.IntegerField(max_length=11)


class Item_reply(models.Model):
    userid = models.IntegerField(max_length=11)
    content = models.TextField()
    editdate = models.DateTimeField()
    taskid = models.IntegerField(max_length=11)
