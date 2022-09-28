from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _
from django_countries.fields import CountryField
from django.dispatch import receiver
from django.db.models.signals import post_save
from utils.generatr_code import generate_code


PHONE_TYPE=(
    ("Primary","Primary"),
    ("Secondary","Secondary"),
   
)


# help function
def upload_img(instance,file_name):
    img_name,ext=file_name.split(".")
    
    return "accounts/%s.%s"%(instance.id,ext)

def phone_validat(value):
    if not len(value)==11:
        raise ValidationError(u'Un valid number.')

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,related_name="user_profile",on_delete=models.CASCADE)
    img=models.ImageField(upload_to=upload_img)
    
    code=models.CharField(max_length=15,default=generate_code)
    used_code=models.BooleanField(default=False)
    active=models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return str(self.user)
    
class ContactNumbers(models.Model):
    user=models.ForeignKey(Profile,related_name="Profile_number",on_delete=models.CASCADE)
    numer=models.CharField(validators=[ RegexValidator(regex=r'^(010|011|012|015)\d{8}$',message="egyption number please")],max_length=11,null=True,blank=True,unique=True)
    type=models.CharField(max_length=15,choices=PHONE_TYPE)
    
    
class DeliveryAddress(models.Model):
    user=models.ForeignKey(Profile,related_name="Profile_adress",on_delete=models.CASCADE)
    country=CountryField()
    city=models.CharField(_('City'),max_length=40)
    state=models.CharField(_('State'),max_length=40)
    region=models.CharField(_('Region'),max_length=40)
    street=models.CharField(_('Street'),max_length=40)
    notes=models.CharField(_('Note'),max_length=100)
 
@receiver(post_save,sender=User)   
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(
            user=instance
        )
        