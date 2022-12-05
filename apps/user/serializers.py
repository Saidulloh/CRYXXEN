from rest_framework import serializers

from apps.user.models import User, Wallet


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
            'is_online'
        )


class ReplenishmentWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        read_only_fileds = ('owner', )
        fields = (
            'id',
            'amount',
            'date',
        )
