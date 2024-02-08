import pyotp 

from django.utils.timezone import datetime, timedelta
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.conf import settings

from rest_framework_simplejwt import tokens
from rest_framework import renderers


def passwordResetEmail(request, user):
    from_email = settings.EMAIL_HOST_USER
    current_site = get_current_site(request)
    mail_subject = 'Forget Password Reset Link'
    message = render_to_string('verification_email.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        "token": tokens.Token(token=request.data["token"]),
    })
    otp_mail_message = renderers.JSONRenderer()
    to_mail = user.email
    mail = EmailMessage(mail_subject, message, from_email, to=[to_mail])
    mail.send()


def sendToken(request):
    totp = pyotp.TOTP(pyotp.random_base32(), interval=180)
    
    otp = totp.now()
    
    request.data["otp_secret_key"] = totp.secret
    
    valid_date = datetime.now() + timedelta(minutes=2)
    
    request.data["otp_valid_date"] = str(valid_date)
    
    print(f"The OTP is : {otp}")
    
    # send a SMS to User's verified Phone number
