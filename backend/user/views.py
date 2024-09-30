from rest_framework import generics, permissions, response, status
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User, Profile
from .serializers import (MYTokenObtainPairSerializer,
                          UserSerializer,
                          RegisterSerializer,
                          ProfileSerializer,)


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    An endpoint for Users to receive access and refresh tokens
    """
    
    serializer_class = MYTokenObtainPairSerializer


class UserRegisterAPIView(generics.CreateAPIView):
    """
    An endpoint for Users to register
    """
    
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class ProfileAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    An endpoint for Users to modify their accounts
    """
    
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        try:
            return Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            raise ValidationError("Profile not found")

    def get(self, request, *args, **kwargs):
        profile = self.get_object()
        srz = ProfileSerializer(profile, many=False)
        return response.Response(data=srz.data, status=status.HTTP_200_OK)
