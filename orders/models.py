from django.db import models
from django.contrib.auth import get_user_model
from utils.generatr_code import generate_code,generate_code_orderes
from django.utils import timezone
from django.utils.text import slugify
from proudct.models import Proudct
# Create your models here.
User=get_user_model()

STATUS=(
    ('recieved','recieved'),
    ('processed','processed'),
    ('shipped','shipped'),
    ('delivered','delivered'),
    
)

class Cart(models.Model):
     code=models.CharField(max_length=8,default=generate_code_orderes)
     user=models.ForeignKey(User,related_name='user_cart',on_delete=models.SET_NULL,blank=True ,null=True)
    
     def save(self,*args,**kwargs):
        self.slug=slugify(self.code)
        super(Cart,self).save(*args,**kwargs)
    
     def get_total(self):
         total=0
         for i in self.cart_detail.all():
             total+=i.total
         return total
    
     def __str__(self) -> str:
        return self.code


class CartDetail(models.Model):
    cart=models.ForeignKey(Cart,related_name='cart_detail',on_delete=models.CASCADE)
    proudct=models.ForeignKey(Proudct,related_name='proudct_cart',on_delete=models.SET_NULL,blank=True ,null=True)
    quantiy=models.IntegerField(default=0)
    price=models.FloatField(default=0)
    total=models.FloatField(default=0)
    slug=models.SlugField(max_length=80,blank=True,null=True,editable=False)
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.cart)
        super(CartDetail,self).save(*args,**kwargs)
    
    def __str__(self) -> str:
        return str(self.cart)


class Order(models.Model):
    code=models.CharField(max_length=8,default=generate_code_orderes)
    user=models.ForeignKey(User,related_name='user_order',on_delete=models.SET_NULL,blank=True ,null=True)
    status=models.CharField(max_length=10,choices=STATUS)
    order_time=models.DateTimeField(default=timezone.now)
    delvery_time=models.DateTimeField(blank=True ,null=True)
    slug=models.SlugField(max_length=80,blank=True,null=True,editable=False)
   
    def save(self,*args,**kwargs):
        self.slug=slugify(self.code)
        super(Order,self).save(*args,**kwargs)
   
    def __str__(self) -> str:
        return self.code
    
class OrderDetail(models.Model):
    order=models.ForeignKey(Order,related_name='order_detail',on_delete=models.CASCADE)
    proudct=models.ForeignKey(Proudct,related_name='proudct_order',on_delete=models.SET_NULL,blank=True ,null=True)
    quantiy=models.IntegerField(max_length=10)
    price=models.FloatField()
    total=models.FloatField()
    slug=models.SlugField(max_length=80,blank=True,null=True,editable=False)
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.order)
        super(OrderDetail,self).save(*args,**kwargs)
    
    def __str__(self) -> str:
        return str(self.order)
    
    
class Cuopon(models.Model):
     code=models.CharField(max_length= 10)
     quantiy=models.IntegerField()
     value=models.FloatField(default=0)
     from_date=models.DateTimeField(default=timezone.now)
     to_date=models.DateTimeField()
     valid=models.BooleanField(default=True)
     
  
     def __str__(self):
        return self.code

     class Meta:
        verbose_name =("Cuopon")
        verbose_name_plural =("Cuopons")
