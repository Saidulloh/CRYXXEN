from rest_framework.routers import DefaultRouter

from apps.basket.views import BasketAPIViewSet, BasketRetrieveUpdateDestroyApiViewSet


router = DefaultRouter()
router.register(
    prefix='',
    viewset=BasketAPIViewSet
)

router.register(
    prefix="",
    viewset=BasketRetrieveUpdateDestroyApiViewSet
)

urlpatterns = router.urls
