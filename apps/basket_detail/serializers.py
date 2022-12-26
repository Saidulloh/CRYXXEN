from rest_framework import serializers

from apps.basket_detail.models import BasketDetail


class BasketDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketDetail
        read_only_field = 'owner'
        fields = (
            'id',
            'product',
            'amount',
        )
