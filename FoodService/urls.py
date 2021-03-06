"""FoodService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include
from django.conf.urls import url
from django.urls import re_path
from django.conf import settings
from django.views.static import serve
from kitchen import views
#from restaurant_admin import apps
#app_name = 'restaurant_admin'
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'kitchen/', include(('kitchen.urls', 'kitchen'), namespace= 'kitchen')),
    url(r'pay/', include(('ZarinPal.urls', 'zarinpal'), namespace= 'zarinpal')),

    #url(r'^customer/', include('customer.urls')),
    url(r'restaurant_ad/', include(('restaurant_admin.urls', 'restaurant_admin'),namespace = 'restaurant_admin')),
    url(r'^$', views.index, name='index'),
]
if settings.DEBUG:
    urlpatterns+= [re_path(r'^media(?P<path>.*)$',
                        serve, {'document_root':
                                 settings.MEDIA_ROOT}),]
