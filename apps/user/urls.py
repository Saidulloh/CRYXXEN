from rest_framework.routers import DefaultRouter

from apps.user.views import UserAPIViewSet, UserUpdateDestroyAPIView


router = DefaultRouter()
router.register(
    prefix="user",
    viewset=UserAPIViewSet
)
router.register(
    prefix="user-edit",
    viewset=UserUpdateDestroyAPIView
)

urlpatterns = router.urls
