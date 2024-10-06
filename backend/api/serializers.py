from rest_framework import serializers
from store.models import Category,Product


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model=Category
        fields=['category_id','title','slug','featured_product','icon']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model=Product
        fields=['id','name','description','image',
                'price','category','inventory',
                'top_deal','flash_sales']
        