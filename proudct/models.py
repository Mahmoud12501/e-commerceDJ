from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.
# Adam 


PROUDCT_FLAG=(
    ('new','new'),
    ('sale','sale'),
    ('feature','feature'),
)


class AdamManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(price__gt=90)

class Proudct(models.Model):
    name=models.CharField(_('Name'),max_length=80)
    sku=models.IntegerField(_('SKU'))
    price=models.FloatField(_('Price'))
    flag=models.CharField(_("Flag"),max_length=15,choices=PROUDCT_FLAG)
    subtitle=models.CharField(_('Subtitle'),max_length=300)
    describtion=models.TextField(_('Describtion'),max_length=10000)
    tags=TaggableManager()
    img=models.ImageField('Image',upload_to='proudct/')
    date_publish=models.DateTimeField(_('Date'),auto_now=True)
    video=models.URLField(_('Video'),null=True,blank=True)
    category=models.ForeignKey('Category',verbose_name= _("Category"),related_name='product_category',on_delete=models.SET_NULL,null=True,blank=True)
    brand=models.ForeignKey('Brand',verbose_name= _("Brand"),related_name='product_brand',on_delete=models.SET_NULL,null=True,blank=True)
    
    
    def __str__(self) -> str:
        return self.name
    
    
    def can(self):
        
        return f"{self.name} >= {self.flag}"
    
    def get_avg(self):
            rate_sum=0
            proudct_review=self.review_product.all()
            for review in proudct_review:
                rate_sum +=review.rate
            avg=rate_sum/len(proudct_review)
            print(avg)
            return avg
    def image_img(self):
     if self.img:
        return u'<img src="%s" width="50" height="50" />' % self.img.url
     else:
        return '(Sin imagen)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True
        
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
    
class Test(models.Model):
    name=models.CharField(max_length=20)
    number=models.CharField(max_length=11)