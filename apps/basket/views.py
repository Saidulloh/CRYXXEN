from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, ListModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.filters import SearchFilter, OrderingFilter

from apps.basket.models import Basket
from apps.basket.serializers import BasketSerializer, BasketCreateSerializer
from apps.basket.permissions import IsOwner


class BasketAPIViewSet(GenericViewSet, 
                    CreateModelMixin, 
                    ListModelMixin):
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
        title = self.request.query_params.get('products__title')
        price = self.request.query_params.get('products__price')
        user_id = self.request.user.id
        if title and price:
            queryset = Basket.objects.filter(owner__id=user_id, products__title__icontains=title, products__price=price)
        elif price:
            queryset = Basket.objects.filter(owner__id=user_id, products__price=price)
        elif title:
            queryset = Basket.objects.filter(owner__id=user_id, products__title__icontains=title)
        else:
            queryset = Basket.objects.filter(owner__id=user_id, is_active=True)
        return set(queryset)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class BasketRetrieveUpdateDestroyApiViewSet(GenericViewSet,
                                        RetrieveModelMixin, 
                                        UpdateModelMixin,
                                        DestroyModelMixin):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = [IsOwner]
