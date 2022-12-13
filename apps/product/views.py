from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter

from apps.product.models import Product
from apps.product.serializers import ProductSerializer
from apps.product.permissions import IsOwner


class ProductApiViewSet(GenericViewSet,
                        ListModelMixin,
                        RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter] # SearchFilter]
    filter_fields = [
            'title',
            'category',
            'time_create',
            'time_update',
            'price'
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
        title = self.request.query_params.get('title')
        price = self.request.query_params.get('price')
        if title and price:
            queryset = Product.objects.filter(title__icontains=title, price=price)
        elif price:
            queryset = Product.objects.filter(price=price)
        elif title:
            queryset = Product.objects.filter(title__icontains=title)
        else:
            queryset = Product.objects.filter(is_active=True)
        return queryset


class ProductDestroyUpdateApiViewSet(GenericViewSet,
                                    DestroyModelMixin,
                                    UpdateModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwner]
