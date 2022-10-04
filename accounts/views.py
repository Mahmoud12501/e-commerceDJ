from django.shortcuts import render, redirect
from django.urls import reverse 
from .forms import SingupForm, ActivateUserForm
from django.contrib.auth import authenticate , login
from .models import Profile
from django.core.mail import send_mail
# Create your views here.

def snignup(request):
    if request.method=="POST":
        form=SingupForm(request.POST)
        if form.is_valid():
          
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password1=form.cleaned_data['password1']
            form.save()
            
            profile=Profile.objects.get(user__username=username)
            profile.active=False
            
            send_mail(
               subject= "confirm your account",
                message=f"yor code to confrim {profile.code} ",
               from_email = "mahmoudn12300@gmail.com",
               recipient_list= [email],
               fail_silently=False,
            )
            print("sent")
            print(email)
            return redirect(f'/accounts/{username}/activate')
            
            # user=authenticate(username=username,password=password1)
            # login(request,user)
            # return redirect("proudct/")
    
        
    return render(request,"registration/signup.html")

def user_activate(request,username):
    user=Profile.objects.get(user__username=username)
    if request.method=='POST':
        form=ActivateUserForm(request.POST)
        if form.is_valid():
            code=form.cleaned_data['code']
            if user.code==code:
                user.active=True
                user.used_code=True
                user.code=' '
                user.save()
                
                return redirect('/accounts/login')
        
    return render(request,"registration/confirm_form.html")
