"""raspy64_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from django.contrib.auth import views as auth_viewspath
from raspy64_backend import views

from .views import (

    # UserGetPhoneView,
    # UserPostView,
    # UserGetUIDView,
    # SendpkView,
    # RandomReqView,
    RealReqView,
    FirstCommView,
)

urlpatterns = [
    path('admin/', admin.site.urls),


    #path('sendpk/', SendpkView.as_view(), name='send_pk'),

    #path('getinitarr/', RandomReqView.as_view(), name='getinitarr'),

    path('getfinalarr/<int:v>/<int:x0>/<int:x1>/',
         RealReqView.as_view(), name='getfinalarr'),
    path('firstcomm/', FirstCommView.as_view(), name='firstcomm'),
]
'''path('getuserphone/<str:id>/<str:pk>/',
         UserGetPhoneView().as_view(), name='get_userphone'),
    path('postuser/<str:id>/<str:Email>/<str:Raspadinha>/<str:Telemovel>/<str:Username>/',
         UserPostView().as_view(), name='post_user'),
    path('getuseruid/<str:email>/<str:pk>',
         UserGetUIDView.as_view(), name='get_useruid'),'''
