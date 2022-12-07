from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

from apps.user.models import User


class UserSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = (
            'id',
            'money',
            'created',
            'is_online',
        )
        fields = (
            'username',
            'last_activity',
            'email',
            'phone_number',
            'birth_date',
            'avatarka',
            'about',
            'password'
        )

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserSerializerList(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'phone_number',
            'birth_date',
            'avatarka',
            'about',
            'created',
            'last_activity',
            'is_online',
        )


class UserSerializerDetail(serializers.ModelSerializer):
    wallet_owner = UserSerializerList(many=True, read_only=True)
    user_favorite = UserSerializerList(many=True, read_only=True)
    basket_owner = UserSerializerList(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'phone_number',
            'birth_date',
            'avatarka',
            'sale',
            'amount',
            'about',
            'created',
            'last_activity',
            'is_online',
            'wallet_owner',
            'user_favorite',
            'basket_owner'
        )


class ResetUserPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField()
    confirm_new_password = serializers.CharField()

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        try:
            user =  User.objects.get(id=validated_data['id'])
            user.set_password(validated_data['new_password'])
            user.save()
            return user
        except User.DoesNotExist:
            return Response(data={"Error": "User can\t found!"}, status=HTTP_404_NOT_FOUND)
