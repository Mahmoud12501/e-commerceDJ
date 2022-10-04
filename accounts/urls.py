from django.urls import path
from . import views

app_name='accounts'

urlpatterns=[
    
    path("singup",views.snignup,name="singup"),
    path("<str:username>/activate",views.user_activate,name='activate'),
    
    
]