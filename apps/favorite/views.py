from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter, SearchFilter

from apps.favorite.models import Favorite
from apps.favorite.serializers import FavoriteSerializer
from apps.favorite.permissions import IsOwner
from apps.product.models import Product


class FavoriteApiViewSet(ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer   
    permission_classes = [IsOwner or IsAuthenticated]
    filter_backends = [OrderingFilter, SearchFilter] 
    filter_fields = [
            'create_at'
            ]         
    ordering_fields = [
            'create_at'
            ]
    search_fields = [
            'product__title'
            ]

    def get_queryset(self):
        queryset = Favorite.objects.filter(user=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        product = Product.objects.get(id = request.data['product'])
        favorite = Favorite.objects.filter(user = request.user).values()
        for i in favorite:
            if product.id == i.get('product_id'):
                return Response({'Error':'There is already such a record!'})
        return super().create(request, *args, **kwargs)
