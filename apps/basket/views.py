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
    filter_backends = [SearchFilter, OrderingFilter, ]
    filter_fields = [
            'product',
            'amount'
            ]
    search_fields = [
            'id',
            'product',
            'amount'
            ]                    
    ordering_fields = [
            'amount',
            'time_create'
            ] 

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = Basket.objects.filter(owner = request.user)
        serializer = BasketSerializer(queryset, many=True)
        total = 0
        context = [[],[]]
        for ser in serializer.data:
            product = Product.objects.get(id=ser['product'])
            one_basket_total = product.price * ser['amount']
            total += one_basket_total
            context[0].append({
                'id':ser['id'],
                'product':ser['product'],
                'time_create':ser['time_create'],
                'amount':ser['amount'],
                'sum':one_basket_total
            })
        context[1].append({'total':total})
            
        return Response(context)

    def create(self, request, *args, **kwargs):
        product = Product.objects.get(id = request.data['product'])
        basket = Basket.objects.filter(owner = request.user).values()
        for i in basket:
            if product.id == i.get('product_id'):
                return Response({'Error':'There is already such a record!'})
        return super().create(request, *args, **kwargs)
