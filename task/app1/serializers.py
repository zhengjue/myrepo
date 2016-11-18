# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models
from rest_framework import serializers
from app1.models import Department
from app1.models import Item
from app1.models import User
from app1.models import Task
from app1.models import Task_reply
from app1.models import Item_reply

class DepartmentSerializar(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('url', 'name')

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields=(
            "url",
            "name",
            "userid" ,
            "itype" ,
            "adddate",
            "startdate",
            "enddate" ,
            "content" ,
            "status" ,
            "del_userid" ,
            "del_status" ,)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields =("name",
            "url",
            "username",
            "passwd",
            "phone",
            "birthday",
            "sex",
            "qq",
            "email",
            "access",
            "image",
            "adddate",
            "status",
            "department",)

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields =(
            "url",
            "inputid"
            "inputdate"
            "userid"
            "depid"
            "assistid"
            "assdepid"
            "subject"
            "content"
            "status"
            "startdate"
            "enddate"
            "begindate"
            "finishdate"
            "evaluate"
            "priority"
            "itemid"
            "departmentid"
            "del_userid"
            "del_status")


class Task_replySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task_reply
        fields =(
            "url",
            "userid",
            "content",
            "editdate",
            "taskid",)


class Item_replySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item_reply
        fields =(
            "url",
            "userid",
            "content",
            "editdate",
            "taskid",)
