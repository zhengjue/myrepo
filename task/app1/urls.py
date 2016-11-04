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
# restfull####################
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from app1 import models

# ##################### User start
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
#################User end##########

#######Test start#################
class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Test
        fields = ('url',  'username', 'password')


# ViewSets define the view behavior.
class TestViewSet(viewsets.ModelViewSet):
    queryset = models.Test.objects.all()
    serializer_class = TestSerializer
#######Test end#############
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tests', TestViewSet)

urlpatterns = [
    url(r'index/', views.index),
    url(r'userlist/', views.userlist),
    url(r'login/', views.login),
    url(r'^', include(router.urls)),
]
