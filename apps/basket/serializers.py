from rest_framework import serializers

from apps.basket.models import Basket
from apps.product.serializers import ProductBasketSerializer


class ProductsDataMixin:

    def __init__(self):
        pass

    @staticmethod
    def get_total(obj):
        lst = []
        for product in obj.products.all():
            if product.amount == 0:
                product.amount = 1
                product.save()
            lst.append(product.price * product.amount)
        return sum(lst)


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

    @staticmethod
    def get_products_data(obj):
        products = obj.products.all()
        return ProductBasketSerializer(products, many=True).data


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
