from rest_framework import serializers
from .models import Proudct ,Brand,Category,ProudctImge,Test

class ProudctSerializer(serializers.ModelSerializer):
    # category =serializers.StringRelatedField()
    # brand =serializers.StringRelatedField()
    class Meta:
        model=Proudct
        fields='__all__'
 
        
class BrandSerializer(serializers.ModelSerializer):
    product_brand=serializers.StringRelatedField()
    class Meta:
        model=Brand
        fields=['name','img','product_brand']



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['name','img','product_category']

class ProudctImgeSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProudctImge
        fields='__all__'
        
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Test
        fields=['pk','name','number']
