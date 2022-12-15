from rest_framework import serializers

from apps.product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        read_only_field = 'owner'
        fields = (
            'id',
            'title',
            'category',
            'image',
            'time_create',
            'time_update',
            'price',
            'is_active'
        )
