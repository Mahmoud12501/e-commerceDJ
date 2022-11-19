from django.shortcuts import render,get_object_or_404
from .models import Cart,CartDetail,Order,OrderDetail,Cuopon
from proudct.models import Proudct
from django.utils.timezone import datetime
# Create your views here.

def add_catr(request):
    if request.method =='POST':
        proudct_id=request.POST['proudct_id']
        quantity=request.POST['quantity']
        
        proudct=Proudct.objects.get(id=proudct_id)
        cart=Cart.objects.get(user=request.user)
        print("save1")
        
        cart_detail,created=CartDetail.objects.get_or_create(cart=cart,proudct=proudct)
        print("save2")
        
        cart_detail.quantiy=int(quantity)
        cart_detail.price=proudct.price
        cart_detail.total=int(proudct.price)*int(quantity)
        cart_detail.save()
        print("save3")

def order_list(request):
    orders=Order.objects.filter(user=request.user)
    return render(request,"orders/orderlist.html",{'orders':orders})


from django.http import JsonResponse
from django.template.loader import render_to_string 
from datetime import date

def checkout(request):
    cart=Cart.objects.get(user=request.user)
    cart_detail=CartDetail.objects.filter(cart=cart)
    
    today=datetime.today().date()
    delevery=30
    if request.method=="POST":
        code=request.POST['code']
        coupon=get_object_or_404(Cuopon,code=code)
        if coupon and coupon.quantiy > 0:
            print("ok")
            print(today)
            print(coupon.from_date)
            print(coupon.to_date)
            
            if  today >= coupon.from_date.date() and  today <= coupon.to_date.date():
                value=(cart.get_total()*coupon.value)/100
                total=delevery+cart.get_total()-value
                
                html=render_to_string("include/recpit.html",{"sub_total":cart.get_total,"total":total,"delevery":delevery,"discount":value, request:request})
                return JsonResponse({"result":html})
        
    return render(request,"orders/checkout.html",{'cart':cart,'cart_detail':cart_detail})

# def mack_coupon(request):
#     if request.method=="POST":
#         code=request.POST['code']
#         coupon=get_object_or_404(Cuopon,code=code)
#         if coupon.from_date <= datetime.now() and coupon.to_date >= datetime.now() and coupon.quantiy!=0:
#            pass 
            
            