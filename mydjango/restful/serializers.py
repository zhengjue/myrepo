#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: serializers.py
# Author: lza
# Created Time: 2016-11-08 17:42:38
############################
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from restful.models import Snippet
# 把snippet对象转化成json数据格式


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'owner','title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    class Meta:
        model = User
        fields = ('url','id', 'username', 'snippets')

if __name__ == "__main__":
    pass

