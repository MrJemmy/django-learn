import os

from django.test import TestCase
from django.contrib.auth.password_validation import validate_password # google it more # we use in user creation
from django.conf import settings # official way but not working here


class DjangoConfigTestCases(TestCase):
    # Django Use Pythons inbuilt unittest methods but with additional Future.
    # def test_anyName(self): # we can create any test by starting with 'test_'
    #     # if any assert Conditions fail then Test result will be failed
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