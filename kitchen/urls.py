from django.conf.urls import url
from . import views
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'Tables_list', views.TableStateListView.as_view(), name='TableState_list' ),
    path(r'Tables_order/<int:pk>/', views.TableOrdersView.as_view(), name='TableOrders' ),
]
