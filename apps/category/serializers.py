from rest_framework import serializers

from apps.category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'


class CategoryFullSerializer(serializers.ModelSerializer):
    product_category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'