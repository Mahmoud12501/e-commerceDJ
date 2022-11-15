from django.urls import include, path
from . import views

app_name='orderes'

urlpatterns = [
    
    path('add-to-cart',views.add_catr,name='add-cart'),
    path("order-list",views.order_list,name="order-list"),
    path("checkout",views.checkout,name="checkout"),
    
    
    
    
]