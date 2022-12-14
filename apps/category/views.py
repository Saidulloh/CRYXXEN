from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAdminUser

from apps.category.models import Category
from apps.category.serializers import CategorySerializer, CategoryFullSerializer


class CategoryApiViewSet(GenericViewSet,
                        ListModelMixin,
                        RetrieveModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    filter_fields = [
            'title',
            ]
    search_fields = [
            'title',
            ]                    
    ordering_fields = [
            'title',
            ]  
    
    def get_serializer_class(self):
        if self.action == 'list':
            return CategorySerializer
        elif self.action == 'retrieve':
            return CategoryFullSerializer
        return super().get_serializer_class()


class CategoryDestroyUpdateApiViewSet(GenericViewSet,
                                    UpdateModelMixin,
                                    DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
