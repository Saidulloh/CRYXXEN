from rest_framework.routers import DefaultRouter

from apps.user.views import UserAPIViewSet, UserUpdateDestroyAPIView, ReplenishmentWalletAPIViewSet


router = DefaultRouter()
router.register(
    prefix="user",
    viewset=UserAPIViewSet
)
router.register(
    prefix="user-edit",
    viewset=UserUpdateDestroyAPIView
)
router.register(
    prefix='replenishment',
    viewset=ReplenishmentWalletAPIViewSet
)

urlpatterns = router.urls
