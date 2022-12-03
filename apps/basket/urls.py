from rest_framework.routers import DefaultRouter

from apps.basket.views import BasketAPIViewSet


router = DefaultRouter()
router.register(
    prefix='',
    viewset=BasketAPIViewSet
)

urlpatterns = router.urls
