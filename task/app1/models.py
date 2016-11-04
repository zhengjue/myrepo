# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Test(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Department(models.Model):
    name = models.CharField(verbose_name="部门名字", max_length=50)

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
    userid = models.IntegerField(blank=True)
    itype = models.CharField(max_length=50)
    adddate = models.DateTimeField(auto_now_add=True)
    startdate = models.DateField(null=True)
    enddate = models.DateField(null=True)
    content = models.TextField(null=True)
    status = models.IntegerField(choices=status_choice,default=0)
    del_userid = models.IntegerField(blank=True)
    del_status = models.IntegerField(choices=del_status_choice,default=0)

    def __unicode__(self):
        return self.name


class User(models.Model):
    sex_choice = (
             (0,'男'),
             (1,'女'),
         )
    user_access_chioce = (
            (0,'普通'),
            (1,'管理员'),
    )
    user_status_choice = (
            (0,'正常'),
            (1,'删除'),
    )
    name = models.CharField(verbose_name="用户名", max_length=20)
    username = models.CharField(verbose_name="登录账号", max_length=50)
    passwd = models.CharField(verbose_name="密码", max_length=50)
    phone = models.IntegerField(verbose_name="电话", null=True)
    birthday = models.DateField(verbose_name="生日", null=True)
    sex = models.IntegerField(verbose_name="性别", choices=sex_choice,default=0)
    qq = models.IntegerField(verbose_name="QQ号码", null=True)
    email = models.EmailField(verbose_name="邮件", null=True)
    access = models.IntegerField(verbose_name="权限", choices=user_access_chioce, default=0)
    image = models.ImageField(verbose_name="头像地址", max_length=50, null=True)
    adddate =models.DateTimeField(verbose_name="加入时间", null=True)
    status = models.IntegerField(verbose_name="用户状态", choices=user_status_choice,default=0)
    department = models.ForeignKey("Department")

    def __unicode__(self):
        return self.name

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
    inputid = models.IntegerField()
    inputdate = models.DateTimeField(null=True)
    userid = models.IntegerField()
    depid = models.IntegerField()
    assistid = models.IntegerField()
    assdepid = models.IntegerField()
    subject = models.CharField(max_length=200)
    content = models.TextField()
    status = models.IntegerField(choices=status_choice,default=0)
    startdate = models.DateTimeField(auto_now_add=True)
    enddate = models.DateTimeField(auto_now_add=True)
    begindate = models.DateTimeField(null=True)
    finishdate = models.DateTimeField(null=True)
    evaluate = models.TextField(null=True)
    priority = models.IntegerField(choices=priority_choice, default=0)
    itemid = models.IntegerField(null=True)
    departmentid = models.IntegerField()
    del_userid = models.IntegerField(null=True)
    del_status = models.IntegerField(choices=status_choice,default=0)


class Task_reply(models.Model):
    userid = models.IntegerField()
    content = models.TextField()
    editdate = models.DateTimeField()
    taskid = models.IntegerField()


class Item_reply(models.Model):
    userid = models.IntegerField()
    content = models.TextField()
    editdate = models.DateTimeField()
    taskid = models.IntegerField()
