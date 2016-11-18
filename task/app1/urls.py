# _*_ coding:utf-8 _*_
"""task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from app1 import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'items', views.ItemViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'departments', views.DepartmentViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'task_replys', views.Task_replyViewSet)
router.register(r'ttem_replys', views.Item_replyViewSet)

urlpatterns = [
    url(r'^index/$', views.Index),
    url(r'^test/$', views.Test),
    url(r'^getuser/$', views.User),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
