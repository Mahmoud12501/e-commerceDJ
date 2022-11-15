from django.shortcuts import render
from .models import Cart,CartDetail,Order,OrderDetail
from proudct.models import Proudct
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


def checkout(request):
    cart=Cart.objects.get(user=request.user)
    cart_detail=CartDetail.objects.filter(cart=cart)
    return render(request,"orders/checkout.html",{'cart':cart,'cart_detail':cart_detail})