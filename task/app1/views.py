# _*_ coding:utf-8  _*_
from django.shortcuts import render, render_to_response,HttpResponse, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import detail_route
from app1 import models
from app1 import serializers

class ItemViewSet(viewsets.ModelViewSet):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializar


class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer


class Item_replyViewSet(viewsets.ModelViewSet):
    queryset = models.Item_reply.objects.all()
    serializer_class = serializers.Item_replySerializer


class Task_replyViewSet(viewsets.ModelViewSet):
    queryset = models.Task_reply.objects.all()
    serializer_class = serializers.Task_replySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    print dir(serializer_class.data)


def Index(request):
        return render_to_response("index.html")

def Test(request):
        return render_to_response("test.html")

def User(request):
        department_result = models.Department.objects.values("id","name")
        #  for k in department_result:
            #  for i ,j in k.items():
                #  print i, j
        return render_to_response("userlist.html", {"department_result": department_result})



# Create your views here.

