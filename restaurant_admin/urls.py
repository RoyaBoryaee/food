from django.conf.urls import url
from . import views
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from django.contrib.auth import views as auth_views
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'login/', auth_views.LoginView.as_view(template_name='restaurant_admin/login.html'),name='login'),
    path(r'change_password/', views.change_password, name='change_password'),
    path(r'logout/', auth_views.LogoutView.as_view(), name='logout'),
    path(r'Home/', views.Home, name='admin_home'),

    path(r'FoodCategory_create',views.FoodCategoryCreateView.as_view(), name='FoodCategory_create'),
    path(r'FoodCategory_update/<int:pk>',views.FoodCategoryUpdateView.as_view(), name='FoodCategory_update'),
    path(r'FoodCategory_delete/<int:pk>',views.FoodCategoryDeleteView.as_view(), name='FoodCategory_delete'),
    path(r'FoodCategory_detail/<int:pk>/',views.FoodCategoryDetailView.as_view(), name='FoodCategory_detail'),

    path(r'FoodCategoryHome_detail',views.FoodCategoryHomeDetailView.as_view(), name='FoodCategoryHome_detail'),

    path(r'Food_create',views.FoodCreateView.as_view(), name='Food_create' ),
    path(r'Food_update/<int:pk>/',views.FoodUpdateView.as_view(), name='Food_update' ),
    path(r'Food_delete/<int:pk>/', views.FoodDeleteView.as_view(), name='Food_delete'),
    path(r'Food_detail/<int:pk>/',views.FoodDetailView.as_view(), name='Food_detail'),

    path(r'FoodHome_detail',views.FoodHomeDetailView.as_view(), name='FoodHome_detail'),


    path(r'Worker_create',views.WorkerCreateView.as_view(), name='Worker_create' ),
    path(r'Worker_list',views.WorkerListView.as_view(), name='Worker_list'),
    path(r'Worker_update/<int:pk>/',views.WorkerUpdateView.as_view(), name='Worker_update' ),
    path(r'Worker_delete/<int:pk>/', views.WorkerDeleteView.as_view(), name='Worker_delete'),
    path(r'Worker_detail/<int:pk>/',views.WorkerDetailView.as_view(), name='Worker_detail'),
    path(r'WorkerHome_detail',views.WorkerHomeDetailView.as_view(), name='WorkerHome_detail'),

    path(r'Table_create',views.TableCreateView.as_view(), name='Table_create' ),
    path(r'Table_list',views.TableListView.as_view(), name='Table_list'),
    path(r'Table_delete/<int:pk>/', views.TableDeleteView.as_view(), name='Table_delete'),
    path(r'Table_detail/<int:pk>/',views.TableDetailView.as_view(), name='Table_detail'),
    path(r'TableHome_detail',views.TableHomeDetailView.as_view(), name='TableHome_detail'),

    path(r'Cost_create',views.CostCreateView.as_view(), name='Cost_create' ),
    path(r'Cost_list',views.CostListView.as_view(), name='Cost_list'),
    path(r'Cost_update/<int:pk>/',views.CostUpdateView.as_view(), name='Cost_update' ),
    path(r'Cost_detail/<int:pk>/', views.CostDetailView.as_view(), name='Cost_detail'),
    path(r'Cost_delete/<int:pk>/', views.CostDeleteView.as_view(), name='Cost_delete'),
    path(r'CostHome_detail',views.CostHomeDetailView.as_view(), name='CostHome_detail'),
]

#urlpatterns += i18n_patterns(path(r'change_password/', views.change_password, name='change_password'),
#)
