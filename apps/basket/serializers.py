from rest_framework import serializers

from apps.basket.models import Basket
from apps.product.serializers import ProductSerializer


class BasketSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField(read_only=True)
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Basket
        read_only_fields = (
            'owner',
        )
        fields = (
            'id',
            'products',
            'time_create',
            'total',
            'products'
        )

    def get_total(self, obj):
        return sum([product.price for product in obj.products.all()])
