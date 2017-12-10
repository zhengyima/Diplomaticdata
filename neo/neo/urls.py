# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import view,search,search2,addc

app_name = 'neo'
urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', search2.search_post),
    url(r'^addindex$', addc.index),
    url(r'^add$', addc.add),
    url(r'^near',view.near),
    url(r'^test$',view.near_test),
    url(r'^find_near',view.find_near),
    url(r'^testnear',view.find_near_before),
    url(r'^path',view.path),
    url(r'^find_path',view.find_path),
    url(r'^is_friends', view.is_friends),
    url(r'^is_entity', view.is_entity),
    url(r'^getEdgeinfo',view.getEdgeinfo),
    url(r'^$',view.near)
]