from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from apps.basket.models import Basket
from apps.basket.serializers import BasketSerializer, BasketCreateSerializer
from apps.basket.permissions import IsOwner


class BasketAPIViewSet(ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = [IsOwner]
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

    def get_serializer_class(self):
        if self.action == 'create':
            return BasketCreateSerializer
        return BasketSerializer

    def get_queryset(self):
        baskets = Basket.objects.filter(owner__id=self.request.user.id)
        for i in baskets:
            print(i.time_create)
        return baskets

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
