from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.basket.models import Basket
from apps.basket.serializers import BasketSerializer
from apps.basket.permissions import IsOwner
from apps.product.models import Product


class BasketAPIViewSet(ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer 
    permission_classes = [IsOwner or IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner = self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = Basket.objects.filter(owner = request.user)
        serializer = BasketSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        product = Product.objects.get(id = request.data['product'])
        basket = Basket.objects.filter(owner = request.user).values()
        for i in basket:
            if product.id == i.get('product_id'):
                return Response({'Error':'There is already such a record!'})
        return super().create(request, *args, **kwargs)
