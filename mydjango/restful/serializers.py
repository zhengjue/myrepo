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
"""
class SnippetSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template':'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=Snippet.LANGUAGE_CHOICES, default="python")
    style = serializers.ChoiceField(choices=Snippet.STYLE_CHOICES, default="friendly")

    def create(self, validated_data):
        #  如果数据合法就创建并返回一个snippet实例
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        #  如果数据合法就更新并返回一个存在的snippet实例
        instance.title = validated_data.get("title",instance.title)
        instance.code = validated_data.get("code",instance.code)
        instance.linenos = validated_data.get("linenos",instance.linenos)
        instance.language = validated_data.get("language",instance.language)
        instance.style = validated_data.get("style",instance.style)
        instance.save()
        return instance
"""


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('url', 'id', 'title', 'code', 'linenos', 'language', 'style')

if __name__ == "__main__":
    pass

