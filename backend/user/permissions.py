from rest_framework import permissions


class CanGetOTP(permissions.BasePermission):
    """
    Check the OTP, if user `is_locked` attribute False, it stop to create new OTP token
    """
    
    def has_permission(self, request, view):
        return request.user.is_locked == True
