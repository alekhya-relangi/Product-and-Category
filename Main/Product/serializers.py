from rest_framework import serializers
from . models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields=('name','parent')
        

        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=('id','name','price','slug','parent')
        

class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=('name','price','parent') 
        
class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"