import pyotp 

from django.utils.timezone import datetime, timedelta


def sendToken(request):
    totp = pyotp.TOTP(pyotp.random_base32(), interval=180)
    
    otp = totp.now()
    
    request.data["otp_secret_key"] = totp.secret
    
    valid_date = datetime.now() + timedelta(minutes=3)
    
    request.data["otp_valid_date"] = str(valid_date)
    
    print(f"The OTP is : {otp}")
    
    # send a SMS to User's verified Phone number
