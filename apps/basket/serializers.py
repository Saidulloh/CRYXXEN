from rest_framework import serializers

from apps.basket.models import Basket
from apps.product.serializers import ProductSerializer


class BasketSerializer(serializers.ModelSerializer):
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
            'products'
        )

    def get_total(self, obj):   
        return sum([product.price for product in obj.products.all()])

    def get_products_data(self, obj):
        produts = obj.products.all()
        return ProductSerializer(produts, many=True).data
