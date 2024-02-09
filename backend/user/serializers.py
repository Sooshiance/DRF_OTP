from rest_framework import serializers

from .models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer class for User
    """
    class Meta:
        model = User
        fields = ["phone", "email", "password", "first_name", "last_name", "pic"]


class LoginSerializer(serializers.Serializer):
    """
    Serializer class for Login
    """
    phone = serializers.CharField(required=True)
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
    otp = serializers.IntegerField(write_only=True, required=True)


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer class for user's profile
    """
    class Meta:
        model = Profile
        fields = "__all__"
