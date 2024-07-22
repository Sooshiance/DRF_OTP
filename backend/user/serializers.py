from rest_framework import serializers

from .models import User, Profile
# Create your serializers here.


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone', 'email', 'first_name', 'last_name']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class TokenSerializer(serializers.Serializer):
    phone    = serializers.CharField()
    password = serializers.CharField(required=False)


class OTPSerializer(serializers.Serializer):
    otp   = serializers.CharField()
    phone = serializers.CharField()
