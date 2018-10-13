# coding: utf8
from django.contrib import admin
from django.urls import (include, path)
from django.conf.urls import url

from rest_framework.authtoken import views

from apps.stations.urls import urlpatterns_v1_locations

from apps.lines.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),

    path('v1/locations/', include(urlpatterns_v1_locations)),

    path('v1/lines/', LinesList.as_view()),
    url('^v1/lines/(?P<pk>[a-z_0-9]+)/$', LineDetail.as_view()),

    path('v1/routes/', RouteList.as_view()),
    url('^v1/routes/(?P<pk>[a-z_0-9]+)/$', RouteDetail.as_view())
]
