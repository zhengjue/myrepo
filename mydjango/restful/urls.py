# _*_ coding:utf-8 _*_
from django.conf.urls import url
from restful import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)
