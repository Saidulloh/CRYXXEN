from rest_framework import serializers

from apps.user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_field = (
            'id',
            'money',
            'last_activity',
            'created',
        )
        fields = (
            'username',
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


class UserSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'phone_number',
            'birth_date',
            'avatarka',
            'money',
            'about',
            'created',
            'last_activity',
        )
