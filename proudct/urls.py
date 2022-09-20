from django.urls import path
from . import views

app_name='proudct'

urlpatterns = [
    path('',views.ProudctListView.as_view(),name='proudct_list'),
    path('<int:pk>',views.ProudctDetailView.as_view(),name='proudct_detail'),
    path('brands',views.BrandListView.as_view(),name='brand_list'),
    path('brands/<int:pk>',views.BrandDetailView.as_view(),name='brand_detail'),
    path('categorys',views.CategoryListView.as_view(),name='category_list'),
    path('categorys/<int:pk>',views.CategoryDetailView.as_view(),name='category_detail'),

    
]