from django.shortcuts import render
from .models import Cart,CartDetail
from proudct.models import Proudct
# Create your views here.

def add_catr(request):
    if request.method =='POST':
        proudct_id=request.POST['proudct_id']
        quantity=request.POST['quantity']
        
        proudct=Proudct.objects.get(id=proudct_id)
        cart=Cart.objects.get_or_create(user=request.user)
        print("save1")
        
        cart_detail,created=CartDetail.objects.get_or_create(cart=cart.id,proudct=proudct.id)
        print("save2")
        
        cart_detail.quantiy=quantity
        cart_detail.price=proudct.price
        cart_detail.total=int(proudct.price)*int(quantity)
        cart_detail.save()
        print("save3")