# _*_ coding:utf-8  _*_
from django.contrib import admin
from app1 import models

# Register your models here.

admin.site.register(models.Department)
admin.site.register(models.Item)
admin.site.register(models.Task)
admin.site.register(models.Item_reply)
admin.site.register(models.Task_reply)
admin.site.register(models.User)
