"""vow URL Configuration

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
from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path,include

#1.导入系统的logging
import logging
# #2.创建（获取）日志器
# logger=logging.getLogger('django')
#
# from django.http import HttpResponse
# def log(request):
#     #3.使用日志器记录信息
#     logger.info('info')
#     return HttpResponse('test')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',log),
    # include 参数1要设置为元组（urlconf_module, app_name）
    # urlconf_module 子应用的路由
    # app_name 子应用的名字
    # namespace 设置命名空间
    path('', include(('users.urls', 'users'), namespace='users')),
]

