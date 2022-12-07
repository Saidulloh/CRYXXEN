from rest_framework.routers import DefaultRouter

from apps.wallet.views import ReplenishmentWalletAPIViewSet


router = DefaultRouter()
router.register(
    prefix='replenishment',
    viewset=ReplenishmentWalletAPIViewSet
)

urlpatterns = router.urls
