from rest_framework import serializers

from apps.favorite.models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Favorite
        read_only_fields = ('user',)
        fields = '__all__'