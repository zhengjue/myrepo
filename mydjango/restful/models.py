# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


# Create your models here.


class Snippet(models.Model):
    LEXERS = [item for item in get_all_lexers() if item[1]]
    LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
    STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

    created = models.DateTimeField(auto_now_add=True, verbose_name="建立时间")
    title = models.CharField(max_length=100, blank=True, verbose_name="标题", default='')
    # blank=True 代表admin管理里是否可以留空
    code = models.TextField(verbose_name="代码")
    linenos = models.BooleanField(default=False, verbose_name="行号")
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100, verbose_name="编程语言")
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100, verbose_name="风格样式")

    # 元类代表对模块在admin 下各种设置，不是单独对某一个域，例如排序啊 搜索等
    class Meta:
        ordering = ('created',)
