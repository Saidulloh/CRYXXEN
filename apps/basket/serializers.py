from rest_framework import serializers

from apps.basket.models import Basket
from apps.product.serializers import ProductSerializer


class ProductsDataMixin:

    def get_total(self, obj):   
        return sum([product.price for product in obj.products.all()])


class BasketSerializer(serializers.ModelSerializer, 
                        ProductsDataMixin):

    total = serializers.SerializerMethodField(read_only=True)
    products_data = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        read_only_fields = (
            'owner',
        )
        fields = (
            'id',
            'time_create',
            'total',
            'products_data',
            'is_active',
        )

    def get_products_data(self, obj):
        produts = obj.products.all()
        return ProductSerializer(produts, many=True).data


class BasketCreateSerializer(serializers.ModelSerializer, 
                            ProductsDataMixin):

    total = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Basket
        fields = (
            'id',
            'time_create',
            'total',
            'products',
            'is_active'
        )
