# _*_ coding:utf-8 _*_


from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ServerAppCateg(models.Model):
    # 前面的文字用于在web作为字段名显示，也可以不写
    id = models.IntegerField(u'服务应用分类ID', primary_key=True, db_column='ID') # Field name made lowercase.
    server_categ_id = models.IntegerField(u'服务功能分类ID')
    app_categ_name = models.CharField(u'服务应用分类名称', max_length=90)
    class Meta:
        # 此模型在数据库实际使用的数据库表名
        db_table = u'server_app_categ'


class ServerFunCateg(models.Model):
    id = models.IntegerField(u'服务功能分类ID', primary_key=True, db_column='ID') # Field name made lowercase.
    server_categ_name = models.CharField(u'服务功能分类名称', max_length=60)
    class Meta:
        db_table = u'server_fun_categ'


class ServerList(models.Model):
    server_name = models.CharField(u'主机名称',max_length=39, primary_key=True)
    server_wip = models.CharField(u'主机外网ip', max_length=45)
    server_lip = models.CharField(u'主机内网ip', max_length=36)
    server_op = models.CharField(u'主机操作系统', max_length=30)
    server_app_id = models.IntegerField(u'服务应用分类ID')
    class Meta:
        db_table = u'server_list'


class ModuleList(models.Model):
    id = models.IntegerField(u'模块ID号', primary_key=True, db_column='ID') # Field name made lowercase.
    module_name = models.CharField(u'模块名称', max_length=60)
    module_caption = models.CharField(u'模块功能描述', max_length=765)
    module_extend = models.CharField(u'模块前端扩展', max_length=6000)
    class Meta:
        db_table = u'module_list'
