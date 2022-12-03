from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.response import Response

from apps.user.models import User
from apps.user.serializers import UserSerializerDetail, UserSerializer


class UserUpdateDestroyAPIView(GenericViewSet,
                            UpdateModelMixin,
                            DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def check(self,request, *args, **kwargs):
        try:
            pk = kwargs.get('pk', None)
            user = User.objects.get(id = pk)
            if user == request.user:
                return Response(data=UserSerializerDetail(user).data)
            return Response({'Error':'You don\'t have pretty permissions!'})
        except User.DoesNotExist:
            return Response({'Error':'Can\'t find user'}, status=HTTP_400_BAD_REQUEST)

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
    serializer_class = UserSerializerDetail

    def get(self, request, *args, **kwargs):
        try:
            queryset = User.objects.get(id=request.user.id)
            serializer = UserSerializerDetail(queryset)
            return Response(data=serializer.data)
        except User.DoesNotExist:   
            return Response({'Error': 'Can\'t find user'}, status=HTTP_400_BAD_REQUEST)
