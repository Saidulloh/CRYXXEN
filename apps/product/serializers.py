from rest_framework import serializers

from apps.product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        read_only_fields = ('owner', 'amount')
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


class ProductBasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'category',
            'image',
            'time_create',
            'time_update',
            'price',
            'is_active',
            'amount',
        )
