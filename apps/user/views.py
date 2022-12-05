from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response

from apps.user.models import User, Wallet
from apps.user.serializers import UserSerializerDetail, UserSerializerCreate, UserSerializerList, ReplenishmentWalletSerializer   


class UserUpdateDestroyAPIView(GenericViewSet,
                            UpdateModelMixin,
                            DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializerCreate

    def check(self,request, *args, **kwargs):
        try:
            pk = kwargs.get('pk', None)
            user = User.objects.get(id = pk)
            if user == request.user:
                return Response(data=UserSerializerDetail(user).data)
            return Response({'Error':'You don\'t have pretty permissions!'})
        except User.DoesNotExist:
            return Response({'Error':'Can\'t find user'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        return self.check(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return self.check(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return self.check(request, *args, **kwargs)


class UserAPIViewSet(GenericViewSet,
                    CreateModelMixin,
                    ListModelMixin,
                    RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializerList

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = User.objects.get(id = kwargs.get('pk'))
            if instance == request.user:
                serializer = UserSerializerDetail(instance)
                return Response(serializer.data)
            return Response(UserSerializerList(instance=instance).data)
        except User.DoesNotExist:
            return Response({'Error': 'Can\'t find user'})

    def get_serializer_class(self):
        if self.action == 'create':
            return UserSerializerCreate
        elif self.action == 'list':
            return UserSerializerList
        elif self.action == 'update':
            return UserSerializerDetail


class ReplenishmentWalletAPIViewSet(GenericViewSet,
                                    CreateModelMixin):
    queryset = Wallet.objects.all()
    serializer_class = ReplenishmentWalletSerializer

    def perform_create(self, serializer):
        return serializer.save(owner = self.request.user)
    
    def create(self, request, *args, **kwargs):
        user = User.objects.get(id = request.user.id)
        amount = int(request.data['amount'])
        user.money += amount
        user.save()
        return super().create(request, *args, **kwargs)
