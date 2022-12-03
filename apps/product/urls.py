from rest_framework.routers import DefaultRouter

from apps.product.views import ProductApiViewSet, ProductDestroyUpdateApiViewSet


router = DefaultRouter()
router.register(
    prefix='product',
    viewset=ProductApiViewSet
)
router.register(
    prefix="",
    viewset=ProductDestroyUpdateApiViewSet
)

urlpatterns = router.urls
