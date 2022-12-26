from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework import status

from apps.basket.models import Basket 
from apps.basket_detail.models import BasketDetail
from apps.basket_detail.serializers import BasketDetailSerializer


class BasketDetailApiViewSet(GenericViewSet,
                            ListModelMixin,
                            RetrieveModelMixin,
                            CreateModelMixin,
                            UpdateModelMixin,
                            DestroyModelMixin):
    queryset = BasketDetail.objects.all()
    serializer_class = BasketDetailSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        basket = Basket.objects.get(owner=request.user)
        product_id = request.data.get('product')
        amount = request.data.get('amount')
        lst = [str(i.id) for i in basket.products.all()]
        if product_id not in lst:
            return Response({'Error': 'You do not have this product in your basket!'})
        else:
            for product in basket.products.all():
                if product_id == str(product.id):
                    product.amount += int(amount)
                    product.save()
                    return Response({'Success': 'Amount of product is successfully added!'})
                else:
                    continue
        serializer = BasketDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        return BasketDetail.objects.filter(owner=self.request.user)
