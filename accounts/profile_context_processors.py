from .models import Profile 
from django.shortcuts import render

def get_profile(request):
    if  request.user.is_authenticated:
        user=Profile.objects.get(user=request.user)
        return {"user_profile":user}
    else:
        return {}