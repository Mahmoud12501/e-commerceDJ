from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.
PROUDCT_FLAG=(
    ('new','new'),
    ('sale','sale'),
    ('feature','feature'),
)

class Proudct(models.Model):
    name=models.CharField(_('Name'),max_length=80)
    sku=models.IntegerField(_('SKU'))
    price=models.FloatField(_('Price'))
    flag=models.CharField(_("Flag"),max_length=15,choices=PROUDCT_FLAG)
    subtitle=models.CharField(_('Subtitle'),max_length=300)
    describtion=models.TextField(_('Describtion'),max_length=10000)
    tags=TaggableManager()
    date_publish=models.DateTimeField(_('Date'),auto_now=True)
    video=models.URLField(_('Video'),null=True,blank=True)
    category=models.ForeignKey('Category',verbose_name= _("Category"),related_name='product_category',on_delete=models.SET_NULL,null=True,blank=True)
    brand=models.ForeignKey('Brand',verbose_name= _("Brand"),related_name='product_Brand',on_delete=models.SET_NULL,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.name
    
class ProudctImge(models.Model):
    proudct=models.ForeignKey('Proudct',verbose_name=_('Proudct'),related_name='img_product',on_delete=models.CASCADE)
    img=models.ImageField(("Image"),upload_to="ProudctImge")
    
    def __str__(self) -> str:
        return str(self.proudct)

class Brand(models.Model):
    name=models.CharField(_('Name'),max_length=80)
    img=models.ImageField(upload_to="Brand")
    
    def __str__(self) -> str:
        return self.name
    
class Category(models.Model):
    name=models.CharField(_('Name'),max_length=80)
    img=models.ImageField(upload_to="Category")
    
    def __str__(self) -> str:
        return self.name
    
    
class ProudctReview(models.Model):
    user=models.ForeignKey(User,related_name='user_review',on_delete=models.SET_NULL,null=True,blank=True)
    proudct=models.ForeignKey('Proudct',verbose_name=_('Proudct'),related_name='review_product',on_delete=models.CASCADE)
    rate=models.IntegerField(_("Rate"))
    review=models.CharField(_('Review'),max_length=300)
    created_at=models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return str(self.proudct)
    