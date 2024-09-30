from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    CustomTokenObtainPairView,
    UserRegisterAPIView,
    ProfileAPIView,
)


app_name = "user"

urlpatterns = [
    path("access/", CustomTokenObtainPairView.as_view(), name='access'),
    path("register/", UserRegisterAPIView.as_view(), name='register'),
    path("profile/", ProfileAPIView.as_view(), name='profile'),
    path("refresh/", TokenRefreshView.as_view(), name='refresh'),
]
