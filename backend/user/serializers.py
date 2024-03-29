from rest_framework import serializers

from .models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer class for User
    """
    class Meta:
        model = User
        fields = ["id", "phone", "email", "password", "first_name", "last_name", "pic"]


class LoginSerializer(serializers.Serializer):
    """
    Serializer class for Login
    """
    phone    = serializers.CharField(required=True)
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': '••••••••••••'}
    )


class OTPSerializer(serializers.Serializer):
    """
    Serializer class for recieving OTP
    """
    phone = serializers.CharField(required=False)
    otp   = serializers.IntegerField(write_only=True, required=True)


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer class for user's profile
    """
    class Meta:
        model = Profile
        fields = "__all__"


class PhoneSerializer(serializers.Serializer):
    """
    Serializer class for getting User's phone to start reset password process
    """
    phone = serializers.CharField(required=True)


class ResetPassowrdSerializer(serializers.Serializer):
    """
    Serializer class for entring the password and confirm one
    """
    password         = serializers.CharField(write_only=True, required=True, help_text='Leave empty if no change needed', style={'input_type': 'password', 'placeholder': '••••••••••••'})
    confirm_password = serializers.CharField(write_only=True, required=True, help_text='Leave empty if no change needed', style={'input_type': 'password', 'placeholder': '••••••••••••'})
