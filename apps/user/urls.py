from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.user.views import UserAPIViewSet, UserUpdateDestroyAPIView, ResetUserPassword, GetUserInfo


router = DefaultRouter()
router.register(
    prefix="user",
    viewset=UserAPIViewSet
)
router.register(
    prefix="user-edit",
    viewset=UserUpdateDestroyAPIView
)

urlpatterns = [
    path("password_reset/", ResetUserPassword.as_view()),
    path('get_user/', GetUserInfo.as_view()),
]

urlpatterns += router.urls
