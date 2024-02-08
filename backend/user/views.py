from rest_framework import permissions, response, status, generics
from rest_framework_simplejwt import tokens

from .permissions import CanGetOTP
from .serializers import *
from .utils import sendToken


####################### TODO : Authentication #######################


class UserLoginAPIView(generics.GenericAPIView):
    """
    An endpoint for users to enter their credentials and recieve OTP
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = []
    
    def post(self, request, *args, **kwargs):
        return response.Response()


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
