from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated


from apps.product.models import Product
from apps.product.serializers import ProductSerializer
from apps.product.permissions import IsOwner


class ProductApiViewSet(GenericViewSet,
                        ListModelMixin,
                        RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)
        return queryset


class ProductDestroyUpdateApiViewSet(GenericViewSet,
                                    DestroyModelMixin,
                                    UpdateModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwner or IsAuthenticated]
