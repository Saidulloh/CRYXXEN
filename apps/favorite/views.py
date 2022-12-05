from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.favorite.models import Favorite
from apps.favorite.serializers import FavoriteSerializer
from apps.favorite.permissions import IsOwner
from apps.product.models import Product


class FavoriteApiViewSet(ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer   
    permission_classes = [IsOwner or IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = Favorite.objects.filter(user = request.user)
        serializer = FavoriteSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        product = Product.objects.get(id = request.data['product'])
        favorite = Favorite.objects.filter(user = request.user).values()
        for i in favorite:
            if product.id == i.get('product_id'):
                return Response({'Error':'There is already such a record!'})
        return super().create(request, *args, **kwargs)
