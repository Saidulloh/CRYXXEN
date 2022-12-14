from rest_framework import serializers

from apps.basket.models import Basket
from apps.product.serializers import ProductSerializer


class BasketSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField(read_only=True)
    prods = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Basket
        read_only_fields = (
            'owner',
        )
        fields = (
            'id',
            'time_create',
            'total',
            'products',
            'prods',
        )

    def get_total(self, obj):
        return sum([product.price for product in obj.products.all()])
