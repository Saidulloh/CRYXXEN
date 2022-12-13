from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

from apps.wallet.models import Wallet
from apps.wallet.serializers import ReplenishmentWalletSerializer
from apps.user.models import User


class ReplenishmentWalletAPIViewSet(GenericViewSet,
                                    CreateModelMixin):
    queryset = Wallet.objects.all()
    serializer_class = ReplenishmentWalletSerializer

    def perform_create(self, serializer):
        return serializer.save(owner = self.request.user)
    
    def create(self, request, *args, **kwargs):
        user = User.objects.get(id = request.user.id)
        amount = int(request.data['amount'])
        user.sale += amount
        user.save()
        return super().create(request, *args, **kwargs)
