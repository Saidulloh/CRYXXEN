from rest_framework import serializers

from apps.basket_detail.models import BasketDetail
from apps.product.serializers import ProductBasketSerializer


class BasketDetailSerializer(serializers.ModelSerializer):
    basket_detail_product = serializers.SerializerMethodField()

    class Meta:
        model = BasketDetail
        read_only_field = 'owner'
        fields = (
            'id',
            'product',
            'amount',
            'basket_detail_product',
        )

    def get_basket_detail_product(self, obj):
        products = obj.product
        return ProductBasketSerializer(products).data
