from django.urls import include, path
from . import views
from . import api
from rest_framework.routers import DefaultRouter


app_name='proudct'


router=DefaultRouter()
router.register('proudct',api.ProudctViewsets)
router.register('brand',api.BrandViewsets)
router.register('category',api.CategoryViewsets)



urlpatterns = [
    path('',views.ProudctListView.as_view(),name='proudct_list'),
    path('<int:pk>',views.ProudctDetailView.as_view(),name='proudct_detail'),
    path('brands',views.BrandListView.as_view(),name='brand_list'),
    path('brands/<int:pk>',views.BrandDetailView.as_view(),name='brand_detail'),
    path('categorys',views.CategoryListView.as_view(),name='category_list'),
    path('categorys/<int:pk>',views.CategoryDetailView.as_view(),name='category_detail'),
    path("all",views.all_proudct,name="all"),
    
    # api
    path('api_list',api.proudct_list_api),
     path('apibrand_list',api.brand_list_api),
     path('api_add/<int:pk>',api.add_pro),
     path('cbv_list',api.Api_list.as_view()),
     path('apitest_list',api.test_list_api),
    path('apitest_pk/<int:pk>',api.test_pk_api),
    # api cbv
    path('cbv_list',api.Test_list.as_view()),
    path('cbv_pk/<int:pk>',api.Test_pk.as_view()),
    # api mixins
    path('mixins_list',api.mixins_list.as_view()),
    path('mixins_pk/<int:pk>',api.mixins_pk.as_view()), 
    
    # genercs
    path('genercs_list',api.generc_list.as_view()),
    path('genercs_pk/<int:pk>',api.generc_pk.as_view()),
    
    # viewsite
    path('proudct_viewsets/',include(router.urls)),
    path('brand_viewsets/',include(router.urls)),
    path('category_viewsets/',include(router.urls)),
    path('searche_proudct',api.searche_proudct),
    
] 