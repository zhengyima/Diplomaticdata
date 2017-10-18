# -*- coding: utf-8 -*-

from django.conf.urls import url

urlpatterns = [
    url(r'^neo/', include('neo.urls',namespace='neo'))
]