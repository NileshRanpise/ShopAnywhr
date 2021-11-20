from store.models import Customer,Product
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'user', 'name', 'locality', 'city', 'zipcode', 'state']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'selling_price', 'discounted_price', 'description', 'brand', 'category','product_image']
