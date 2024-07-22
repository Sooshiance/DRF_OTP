import datetime
from django.utils import timezone

import pyotp

from .models import OTP


def sendToken(user):
    try:
        otp = OTP.objects.get(user=user)
        access_time = (datetime.timedelta(minutes=1) + otp.created_at).timestamp()
        delta_time = access_time - timezone.now().timestamp()
        if delta_time > 0:
            return {'error': f"waite : {delta_time} seconds", 'otp': False}
        else:
            otp.delete()
    except OTP.DoesNotExist:
        pass

    totp = pyotp.TOTP(pyotp.random_base32(), interval=60)

    otp = totp.now()

    OTP.objects.create(user=user, otp=otp).save()

    return {'otp': otp, 'error': False}
