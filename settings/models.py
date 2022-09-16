from django.db import models

# # Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=50)
    subtitle=models.CharField(max_length=500)
    logo=models.ImageField(upload_to='logo/')
    call_us=models.CharField(max_length=15)
    email_us=models.EmailField()
    email=models.TextField(max_length=200)
    phone=models.TextField(max_length=200)
    adress=models.TextField(max_length=400)
    fb_link=models.URLField(max_length=300)
    instagram_link=models.URLField(max_length=300)
    tw_link=models.URLField(max_length=300)
    pentrist_link=models.URLField(max_length=300)
    
    def __str__(self) -> str:
        return self.name