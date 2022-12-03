from rest_framework.routers import DefaultRouter

from apps.category.views import CategoryApiViewSet, CategoryDestroyUpdateApiViewSet


router = DefaultRouter()
router.register(
    prefix='category',
    viewset=CategoryApiViewSet
)
router.register(
    prefix='',
    viewset=CategoryDestroyUpdateApiViewSet
)

urlpatterns = router.urls
