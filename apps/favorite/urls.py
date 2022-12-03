from rest_framework.routers import DefaultRouter

from apps.favorite.views import FavoriteApiViewSet


router = DefaultRouter()
router.register(
    prefix='',
    viewset=FavoriteApiViewSet
)

urlpatterns = router.urls
