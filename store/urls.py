from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


schema_view = get_swagger_view(title='CRYXXEN API')

api_urlpatterns = [
    path('baskets/', include('apps.basket.urls')),
    path('categories/', include('apps.category.urls')),
    path('favorites/', include('apps.favorite.urls')),
    path('products/', include('apps.product.urls')),
    path('users/', include('apps.user.urls')),
    path('wallets/', include('apps.wallet.urls')),

    # tokens
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]


urlpatterns = [
    path('admin/', admin.site.urls),

    # swagger
    path('swagger/', schema_view),
    
    # Authorization
    path("api/", include(api_urlpatterns))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
