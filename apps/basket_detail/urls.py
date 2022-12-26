from rest_framework.routers import DefaultRouter

from apps.basket_detail.views import BasketDetailApiViewSet


router = DefaultRouter()
router.register(
    prefix="",
    viewset=BasketDetailApiViewSet
)

urlpatterns = router.urls
