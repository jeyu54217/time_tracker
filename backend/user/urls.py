from django.urls import path
from .views import (UserRegistrationView, 
                    VerifyEmailView, 
                    GoogleOAuth2CallbackView, 
                    LogoutView,
                    )

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user_register'),
    path('verify_email/', VerifyEmailView.as_view(), name='verify_email'),
    path('callback/', GoogleOAuth2CallbackView.as_view(), name='GoogleOAuth2Callback'),
    path('logout/', LogoutView.as_view(), name='logout')
    ]
