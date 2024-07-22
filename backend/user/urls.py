from django.urls import path

from .views import (
    RequestOtpAPIView,
    CheckOtpAPIView
)


app_name = 'user'

urlpatterns = [
    path('request/token/', RequestOtpAPIView.as_view(), name='request-token'),

    path('check/token/', CheckOtpAPIView.as_view(), name='check-token'),
]
