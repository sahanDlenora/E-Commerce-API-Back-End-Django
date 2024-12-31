from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, CartViewSet, OrderViewSet

# Create a router and register your viewsets
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'cart', CartViewSet)
router.register(r'orders', OrderViewSet)

# Include both the router-generated URLs and the manually defined URLs
urlpatterns = [
    # JWT Token URLs
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Registration URL
    path('register/', RegisterView.as_view(), name='register'),

    # Router URLs for viewsets (automatic routing)
    path('api/', include(router.urls)),  # All viewsets are accessible under 'api/'
]
