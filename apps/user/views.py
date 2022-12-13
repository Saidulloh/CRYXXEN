from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_202_ACCEPTED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from apps.user.models import User
from apps.user.serializers import UserSerializerDetail, UserSerializerCreate, UserSerializerList, ResetUserPasswordSerializer   


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

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = User.objects.get(id = kwargs.get('pk'))
            if instance == request.user:
                return Response(UserSerializerDetail(instance).data)
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


class ResetUserPassword(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = ResetUserPasswordSerializer(data=request.data)
            if serializer.is_valid():
                if request.data['new_password'] == request.data['confirm_new_password']:
                    if request.data['new_password'].isalnum():
                        user = User.objects.get(id=request.user.id)
                        user.set_password(request.data['new_password'])
                        user.save()
                        return Response(data={"ok": "ok"}, status=HTTP_202_ACCEPTED)
                else:
                    return Response(data={"Error":"Password is not confirmed"}, status=HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response(data={"error": f"error is {ex}"}, status=HTTP_400_BAD_REQUEST)


class GetUserInfo(ListAPIView):
    queryset = User.objects.filter(id=False)
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializerList

    def get(self, request, *args, **kwargs):
        queryset = User.objects.get(id=request.user.id)
        if queryset:
            serializer = UserSerializerDetail(queryset)
            return Response(data=serializer.data)
        return Response({'error': 'Bad request'}, status=HTTP_400_BAD_REQUEST)
