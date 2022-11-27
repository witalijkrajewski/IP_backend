from rest_framework import serializers
from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

        fields = (
            'id',
            'category',
            'get_full_name',
            'get_absolute_url',
            'price',
            'equipment',
            'description',
            'get_image1',
            'get_image2',
            'get_image3',
            'get_image4',
            'get_thumbnail',
        )

