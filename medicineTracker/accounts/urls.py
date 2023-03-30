from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('verifyotp/', VerfiyOTPView.as_view()),
    path('login/', LoginView.as_view()),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/',  TokenVerifyView.as_view(), name='token_verify'),
    # path('register/', RegisterView.as_view()),
    # path('profile/', ProfileView.as_view())
]