from rest_framework.test import APITestCase

from user.models import User, Profile


class TestUser(APITestCase):
    def setUp(self):
        # TODO : Data for mocking model
        self.credentials1 = {'phone':'09121234567',
                            "email":'test@example.com',
                            "first_name":'علی',
                            "last_name":'علی'
                            }
        
        self.user1 = User.objects.create_user(**self.credentials1)
    
    # TODO : Test scenarios for the user 1
    def test_user1_creation(self):
        self.assertEqual(self.user1.phone, '09121234567')
        self.assertEqual(self.user1.email, 'test@example.com')
    
    def test_user1_full_name(self):
        self.assertEqual(self.user1.fullName, 'علی علی')
    
    def test_user1_has_perm(self):
        self.assertTrue(self.user1.has_perm('any_perm'))
    
    def test_user1_is_active(self):
        self.assertTrue(self.user1.is_active)
    
    def test_user1_is_superuser(self):
        self.assertFalse(self.user1.is_superuser)
    
    def test_update_user1(self):
        pass


class TestProfile(APITestCase):

    def setUp(self):
        # TODO : Data for mocking model
        self.user_credentials = {'phone':'09121234568',
                            "email":'test1@example.com',
                            "first_name":'شمس',
                            "last_name":'نور'
                            }
        self.user = User.objects.create_user(**self.user_credentials)

    def test_profile_creation(self):
        p = Profile.objects.get(user=self.user)
        self.assertEqual(p.phone, '09121234568')
    
    def test_update_profile_phone(self):
        p = Profile.objects.get(user=self.user)
        new_phone = "09129876543"
        p.phone = new_phone
        p.save()
        self.assertEqual(p.phone, "09129876543")
