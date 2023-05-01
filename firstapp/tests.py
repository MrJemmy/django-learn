from django.test import TestCase
from django.contrib.auth.password_validation import validate_password # google it more
from django.conf import settings # official way but not working here
import os

# Create your tests here.
class djangoConfigTest(TestCase):
    # def test_anyName(self): # we can create any test by starting with 'test_'
    #     self.assertTrue(1==1)
    #     self.assertFalse(1==2)
    #     self.assertIsNone(None)
    #     self.assertIsNotNone(not None)
    #     self.assertEqual(1,1)
    #     self.assertNotEqual(1,2)
    #     self.fail() use in try except to fail test_case

    def test_secret_key_strength(self):
        SECRET_KEY = os.environ.get("SECRET_KEY")
        try:
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            msg = f"bad secret key : {e}"
            self.fail(msg)

