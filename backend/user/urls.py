from django.urls import path

from .views import *


urlpatterns = [
    # Auth generics
    path('login/', UserLoginAPIView.as_view()),
    path('login/otp/', OTPLoginAPIView.as_view()),
    path('auth/user/', AuthenticatedAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    
    # Register generics
    path('register/', RegisterAPIView.as_view()),
    path('register/otp/', ActivateAccountAPIView.as_view()),
    
    # OTP reset password
    path('phone-verify/', VerifyPhonExistAPIView.as_view()),
    path('phone-verify/otp/', OTPVerifyAPIView.as_view()),
    path('reset-otp-link/', OTPResetLinkAPIView.as_view()),
    
    # Email reset password
    path('email-verify/', VerifyEmailExistAPIView.as_view()),
    path('email-verify/otp/', EmailVerifyAPIView.as_view()),
    path('reset-email-link/', EmailResetLinkAPIView.as_view()),
]
