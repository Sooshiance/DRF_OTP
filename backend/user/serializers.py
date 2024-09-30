from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token

from .models import User, Profile


class MYTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user: User) -> Token:
        token = super().get_token(user)
        token['id'] = user.pk
        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['is_active', 'is_staff', 'is_superuser']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
