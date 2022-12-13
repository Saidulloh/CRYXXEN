from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

from apps.product.models import Product
from apps.product.serializers import ProductSerializer
from apps.product.permissions import IsOwner


class ProductApiViewSet(GenericViewSet,
                        ListModelMixin,
                        RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter, ]
    filter_fields = [
            'title',
            'category',
            'time_create',
            'time_update',
            'price'
            ]
    search_fields = [
            'title',    
            '=price'
            ]                    
    ordering_fields = [
            'title',
            'category',
            'time_create',
            'time_update',
            'price',
            ] 


    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        price = self.request.query_params.get('search')
        queryset = Product.objects.filter(is_active=True)
        return queryset


class ProductDestroyUpdateApiViewSet(GenericViewSet,
                                    DestroyModelMixin,
                                    UpdateModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwner]
