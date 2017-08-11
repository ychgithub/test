"""sitetest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from users.views import index,forget,logintest,new,logouttest,active
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index,name='index'),
    # 这个容易出错
    url(r'^login/$',logintest.as_view(),name='login'),
    url(r'^logout/$',logouttest,name='logout'),
    url(r'^forget/$',forget.as_view(),name='forget'),
    url(r'^new/$',new.as_view(),name='new'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<code_back>.*)/$',active.as_view(),name='active'),
    # 利用正则表达式,将active之后的所有内容,赋值给变量code_back,并且传递过去.
]
