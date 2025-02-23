from rest_framework import serializers
from .models import Category, Product


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "get_image",
            "get_thumbnail",
            "price",
            "description"
        )

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializers(many=True)
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "products",
            "get_absolute_url"
        )