from rest_framework import serializers

from apps.basket.models import Basket
from apps.product.serializers import ProductSerializer


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        read_only_fields = (
            'owner',
        )
        fields = (
            'id', 
            'product',
            'time_create',
            'amount'
        )
