from django.test import TestCase
# from django.conf import settings
import os
from django.contrib.auth.password_validation import validate_password

class TryDjangoConfigTest(TestCase):
    # def test_secret_key_strength(self):
    #     SECRET_KEY = os.environ.get('SECRET_KEY')
    #     # self.assertNotEqual(SECRET_KEY, 'abc123')
    #     try: 
    #         is_strong = validate_password(SECRET_KEY)
    #     except Exception as e:
    #         msg = f'Weak Secret Key {e.messages}'
    #         self.fail(msg)

    def test_secret_key_strength(self):
        SECRET_KEY = os.environ.get('SECRET_KEY')
    # 1. Make sure it exists
        self.assertIsNotNone(SECRET_KEY)
    # 2. Make sure it's not the default insecure one
        self.assertNotEqual(SECRET_KEY, 'django-insecure-default-key')  