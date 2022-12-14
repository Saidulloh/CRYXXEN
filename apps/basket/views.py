from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

from apps.basket.models import Basket
from apps.basket.serializers import BasketSerializer
from apps.basket.permissions import IsOwner
from apps.product.models import Product


class BasketAPIViewSet(ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = [IsOwner or IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    filter_fields = [
        'time_create'
    ]
    ordering_fields = [
        'time_create'
    ]
    search_fields = [
        'products__title',
        'products__price'
    ]

    def get_queryset(self):
        return Basket.objects.filter(owner__id=self.request.user.id)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
