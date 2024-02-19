from django.contrib.auth import authenticate

from rest_framework import permissions, response, status, generics, renderers
from rest_framework_simplejwt import tokens

from .models import User , OTP
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
                user = User.objects.get(phone=phone)
                otp_token = sendToken(user=user)
                OTP.objects.create(user=user,otp=otp_token).save()
                return response.Response(data=request.data, status=status.HTTP_202_ACCEPTED)
            else:
                return response.Response("User does not exist!", status=status.HTTP_404_NOT_FOUND)
        else:
            return response.Response(data=s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class OTPLoginAPIView(generics.GenericAPIView):
    """
    An endpoint for users to evaluate their OTP token
    """
    permission_classes = []
    serializer_class = [OTPSerializer]
    
    def post(self, request, *args, **kwargs):
        s = OTPSerializer(data=request.data)
        if s.is_valid():
            otp = s.validated_data["otp"]
            phone = s.validated_data["phone"]
            if OTP.objects.get(otp=otp):
                uo = OTP.objects.get(otp=otp)
                print(uo)
                user = User.objects.get(phone=uo)
                token = tokens.RefreshToken.for_user(user)
                data = s.data
                data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}                
                uo.delete()
                return response.Response(data, status=status.HTTP_205_RESET_CONTENT)
            else:
                return response.Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return response.Response(s.errors, status=status.HTTP_408_REQUEST_TIMEOUT)


class AuthenticatedAPIView(generics.GenericAPIView):
    """
    An endpoint for authenticated users
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = [ProfileSerializer]
    
    def post(self, request, *args, **kwargs):
        user = request.user.pk 
        p = Profile.objects.get(user=user)
        s = ProfileSerializer(data=p)
        return response.Response(data=s.data, status=status.HTTP_200_OK)


class LogoutAPIView(generics.GenericAPIView):
    """
    An endpoint for users to logout from system
    """
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = tokens.RefreshToken(refresh_token)
            token.blacklist()
            return response.Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)


####################### TODO : Registeration #######################


class RegisterAPIView(generics.GenericAPIView):
    """
    An endpoint for users to register their account
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = [UserSerializer]
    
    def post(self, request, *args, **kwargs):
        s = UserSerializer(data=request.data)
        if s.is_valid():
            s.save()
            otp = sendToken(user=s.data)
            return response.Response(data=s.data, status=status.HTTP_201_CREATED)
        else:
            return response.Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class ActivateAccountAPIView(generics.GenericAPIView):
    """
    An endpoint to activate their account via OTP 
    """
    permission_classes = []
    serializer_class = [OTPSerializer]
    
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
    serializer_class = [OTPSerializer]
    
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
    renderer_classes = []
    
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
