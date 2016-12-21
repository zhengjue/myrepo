# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-21 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModuleList',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('module_name', models.CharField(max_length=60, verbose_name='\u6a21\u5757\u540d\u79f0')),
                ('module_caption', models.CharField(max_length=765, verbose_name='\u6a21\u5757\u529f\u80fd\u63cf\u8ff0')),
                ('module_extend', models.CharField(max_length=6000, verbose_name='\u6a21\u5757\u524d\u7aef\u6269\u5c55')),
            ],
            options={
                'db_table': 'module_list',
            },
        ),
        migrations.CreateModel(
            name='ServerAppCateg',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('server_categ_id', models.IntegerField()),
                ('app_categ_name', models.CharField(max_length=90, verbose_name='\u670d\u52a1\u5e94\u7528\u5206\u7c7b\u540d\u79f0')),
            ],
            options={
                'db_table': 'server_app_categ',
            },
        ),
        migrations.CreateModel(
            name='ServerFunCateg',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('server_categ_name', models.CharField(max_length=60, verbose_name='\u670d\u52a1\u529f\u80fd\u5206\u7c7b\u540d\u79f0')),
            ],
            options={
                'db_table': 'server_fun_categ',
            },
        ),
        migrations.CreateModel(
            name='ServerList',
            fields=[
                ('server_name', models.CharField(max_length=39, primary_key=True, serialize=False, verbose_name='\u4e3b\u673a\u540d\u79f0')),
                ('server_wip', models.CharField(max_length=45, verbose_name='\u4e3b\u673a\u5916\u7f51ip')),
                ('server_lip', models.CharField(max_length=36, verbose_name='\u4e3b\u673a\u5185\u7f51ip')),
                ('server_op', models.CharField(max_length=30, verbose_name='\u4e3b\u673a\u64cd\u4f5c\u7cfb\u7edf')),
                ('server_app_id', models.IntegerField()),
            ],
            options={
                'db_table': 'server_list',
            },
        ),
    ]
