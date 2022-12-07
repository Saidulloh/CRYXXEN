from rest_framework import serializers

from apps.wallet.models import Wallet


class ReplenishmentWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        read_only_fileds = ('owner', )
        fields = (
            'id',
            'amount',
            'date',
        )