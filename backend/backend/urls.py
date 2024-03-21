
from django.contrib import admin
from user.views import UserRegistrationView, VerifyEmailView, GoogleOAuth2CallbackView
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', UserRegistrationView.as_view(), name='user_register'),
    path('api/verify_email/', VerifyEmailView.as_view(), name='verify_email'),
    path('auth/google/callback', GoogleOAuth2CallbackView.as_view(), name='GoogleOAuth2Callback'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    ]