from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

from apps.category.models import Category
from apps.category.serializers import CategorySerializer
from apps.category.permissions import IsOwner


class CategoryApiViewSet(GenericViewSet,
                        ListModelMixin,
                        RetrieveModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []


class CategoryDestroyUpdateApiViewSet(GenericViewSet,
                                    UpdateModelMixin,
                                    DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsOwner]
