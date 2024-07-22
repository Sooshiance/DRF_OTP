from datetime import timedelta

from django.utils import timezone
from django.shortcuts import get_object_or_404

from rest_framework import permissions, response, status, generics
from rest_framework_simplejwt import tokens

from .models import User, OTP
from .serializers import TokenSerializer, OTPSerializer
from .utils import sendToken


class RequestOtpAPIView(generics.GenericAPIView):
    """
    An endpoint for users to request OTP tokens
    """

    permission_classes = (permissions.AllowAny,)
    serializer_class = TokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = TokenSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data["phone"]
            user = get_object_or_404(User, phone=phone)
            # TODO : Check if user has already otp token in OTP model
            if not OTP.objects.filter(user=user):
                result = sendToken(user=user)
                otp = result['otp']
                error = result['error']
                if otp:
                    print(f"The OTP is : {otp}")
                    return response.Response({"mobile": user.phone[-4:]},
                                             status=status.HTTP_200_OK)
                else:
                    return response.Response(
                        {"waite": error},
                        status=status.HTTP_429_TOO_MANY_REQUESTS)
            else:
                user_otp = OTP.objects.filter(user=user)
                for obj in user_otp:
                    # TODO : Delete user otp tokens that created
                    # 2 minutes ago or later
                    # 2 min = 1 min (token expire time) + 1 min(cool down
                    # for requesting new token)
                    if timedelta(minutes=2) >= timezone.now() - obj.created_at:
                        obj.delete()
                return response.Response(
                    {"otp exist"}, status=status.HTTP_429_TOO_MANY_REQUESTS)
        return response.Response(serializer.errors,
                                 status=status.HTTP_400_BAD_REQUEST)


class CheckOtpAPIView(generics.GenericAPIView):
    """
    An endpoint for users to send their OTP tokens
    """

    serializer_class = OTPSerializer

    def post(self, request, *args, **kwargs):
        serializer = OTPSerializer(data=request.data)
        if serializer.is_valid():
            otp = serializer.validated_data["otp"]
            phone = serializer.validated_data["phone"]
            user_otp = get_object_or_404(OTP, user__phone=phone)
            counter = user_otp.counter
            if user_otp.otp == otp and counter > 0:
                # TODO: We need to calculate the token expiration time
                otp_created_time = user_otp.created_at
                current_time = timezone.now()
                time_difference = current_time - otp_created_time
                if time_difference < timezone.timedelta(minutes=2):
                    user = user_otp.user
                    token = tokens.RefreshToken.for_user(user)
                    data = {"refresh": str(token),
                            "access": str(token.access_token)}
                    user_otp.delete()
                    return response.Response(
                        data, status=status.HTTP_205_RESET_CONTENT)
                else:
                    user_otp.delete()
            else:
                if counter < 0:
                    user_otp.delete()
                else:
                    user_otp.counter -= 1
                    user_otp.save()
            return response.Response({
                'error': "Token has been expired"},
                status=status.HTTP_408_REQUEST_TIMEOUT)
        else:
            return response.Response(
                serializer.errors, status=status.HTTP_408_REQUEST_TIMEOUT)
