from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView, PublicHelloView, ProtectedHelloView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('public-hello/', PublicHelloView.as_view(), name='public-hello'),
    path('protected-hello/', ProtectedHelloView.as_view(), name='protected-hello'),

    # JWT Token endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
