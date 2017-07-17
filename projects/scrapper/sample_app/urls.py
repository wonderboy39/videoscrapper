# -*- coding: utf-8 -*-
from django.conf.urls import url
from sample_app import views
from sample_app.views import VideoUrlUpdateView, VideoUpdateView, VideoUrlCategoryUpdateView

#app_name = 'sample_app'
urlpatterns = [
    url(r'^/$', views.index, name='index'),
    url(r'^write/$', views.write, name='write'),
    url(r'^write_ok/$', views.write_ok, name='write_ok'),
    url(r'^show_vlist/$', views.show_vlist, name='show_vlist'),
    url(r'^modify/$', views.modify, name='modify'),
    url(r'^modify_ok/$', views.modify_ok, name='modify_ok'),
    # Category 사용하는 url pattern
    url(r'^(?P<pk>[0-9]+)/edit/$', VideoUrlCategoryUpdateView.as_view(), name='edit'),
    # Category 사용하지 않는 url pattern, UpdateView 클래스 사용
    url(r'^(?P<pk>[0-9]+)/update/$', VideoUrlUpdateView.as_view(), name='update'),
    # View 클래스 이용
    url(r'^(?P<pk>[0-9]+)/mupdate/$', VideoUpdateView.as_view(), name='mupdate'),
]
