from django.urls import reverse
from django.http import Http404

from rest_framework.test import APITestCase, APIClient

from user.models import User, OTP


class TestLoginAPIView(APITestCase):

    def setUp(self):
        self.credentials = {"phone": "09121234566",
                            "email": "testing@gmail.com",
                            "first_name": "هادی",
                            "last_name": "احمد",
                            }
        self.client = APIClient()
        self.get_otp = reverse("user:request-token")
        self.confirm_otp = reverse("user:check-token")
        self.user = User.objects.create_user(**self.credentials)

    def test_otp(self):

        response = self.client.post(self.get_otp, {"phone": f'{self.user.phone}'})

        # print(response.headers)

        self.assertEqual(response.status_code, 200)

        otp = OTP.objects.get(user=self.user)

        print(f"OTP =========== {otp.otp}")

        try:

            otp_token = otp.otp

            response1 = self.client.post(self.confirm_otp, {
                "phone": self.user.phone, "otp": otp_token})

            self.assertEqual(response1.status_code, 205)

        except otp.DoesNotExist:

            raise Http404("The OTP token does not exist!")
