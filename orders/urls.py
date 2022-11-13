from django.urls import include, path
from . import views

app_name='orderes'

urlpatterns = [
    
    path('add-to-cart',views.add_catr,name='add-cart')
    
    
]