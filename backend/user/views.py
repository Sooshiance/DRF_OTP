from django.contrib.auth import authenticate

from rest_framework import permissions, response, status, generics
from rest_framework_simplejwt import tokens

from .models import User 
from .permissions import CanGetOTP
from .serializers import *
from .utils import sendToken


####################### TODO : Authentication #######################


class UserLoginAPIView(generics.GenericAPIView):
    """
    An endpoint for users to enter their credentials and recieve OTP
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = [LoginSerializer]
    
    def post(self, request, *args, **kwargs):
        s = LoginSerializer(data=request.data)
        if s.is_valid():
            phone = s.validated_data["phone"]
            password = s.validated_data["password"]
            
            if authenticate(request=request, phone=phone, password=password):
                user = authenticate(request=request, phone=phone, password=password)
                sendToken(request=request)
                return response.Response(data=user, status=status.HTTP_202_ACCEPTED)
            else:
                return response.Response("User does not exist!", status=status.HTTP_404_NOT_FOUND)
        else:
            return response.Response(data=s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class OTPLoginAPIView(generics.GenericAPIView):
    """
    An endpoint for users to evaluate their OTP token
    """
    permission_classes = []
    serializer_class = []
    
    def post(self, request, *args, **kwargs):
        return response.Response()


class AuthenticatedAPIView(generics.GenericAPIView):
    """
    An endpoint for authenticated users
    """
    permission_classes = []
    serializer_class = []
    
    def post(self, request, *args, **kwargs):
        return response.Response()


class LogoutAPIView(generics.GenericAPIView):
    """
    An endpoint for users to logout from system
    """
    permission_classes = []
    
    def post(self, request, *args, **kwargs):
        return response.Response()


####################### TODO : Registeration #######################


class RegisterAPIView(generics.GenericAPIView):
    """
    An endpoint for users to register their account
    """
    permission_classes = []
    serializer_class = []
    
    def post(self, request, *args, **kwargs):
        return response.Response()


class ActivateAccountAPIView(generics.GenericAPIView):
    """
    An endpoint to activate their account via OTP 
    """
    permission_classes = []
    serializer_class = []
    
    def post(self, request, *args, **kwargs):
        return response.Response()


####################### TODO : Reset_Password via OTP #######################


class VerifyPhonExistAPIView(generics.GenericAPIView):
    """
    An endpoint to 
    """
    permission_classes = []
    serializer_class = []
    
    def post(self, request, *args, **kwargs):
        return response.Response()


class OTPVerifyAPIView(generics.GenericAPIView):
    """
    An endpoint to check users OTP
    """
    permission_classes = []
    serializer_class = []
    
    def post(self, request, *args, **kwargs):
        return response.Response()


class OTPResetLinkAPIView(generics.GenericAPIView):
    """
    An endpoint to reset their password
    """
    permission_classes = []
    serializer_class = []
    
    def post(self, request, *args, **kwargs):
        return response.Response()


####################### TODO : Reset_Password via Email #######################


class VerifyEmailExistAPIView(generics.GenericAPIView):
    """
    An endpoint to check and send user reset link
    """
    permission_classes = []
    serializer_class = []
    
    def post(self, request, *args, **kwargs):
        return response.Response()


class EmailVerifyAPIView(generics.GenericAPIView):
    """
    An endpoint to evaluate users Email
    """
    permission_classes = []
    serializer_class = []
    
    def post(self, request, *args, **kwargs):
        return response.Response()


class EmailResetLinkAPIView(generics.GenericAPIView):
    """
    An endpoint to reset their password
    """
    permission_classes = []
    serializer_class = []
    
    def post(self, request, *args, **kwargs):
        return response.Response()
