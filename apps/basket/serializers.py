from rest_framework import serializers

from apps.basket.models import Basket


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
        )
