from django.urls import path,include
from . import views

app_name='proudct'

urlpatterns = [
    path('',views.ProudctListView.as_view(),name='proudct_list'),
    path('<int:pk>',views.ProudctDetailView.as_view(),name='proudct_detail'),
    
]