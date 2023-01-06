import time

from django.test import TestCase
from django.urls import reverse
from django.core.cache import cache
from rest_framework.test import APITestCase, RequestsClient


class SignupFlowTestCase(APITestCase):
    SIGNUP_ENDPOINT = 'signup'
    VERIFY_ENDPOINT = 'verify'
    SIGNIN_ENDPOINT = 'signin'

    def test_signup_user(self):
        self.data = {
            'email': 'testcase@test.com',
            'phone': '09199142330',
            'password': '12345678',
        }
        response = self.client.post(reverse(self.SIGNUP_ENDPOINT), self.data)
        self.assertEqual(response.status_code, 201)

    def test_verify_user_phone(self):
        time.sleep(0.009)
        code = cache.get(self.data.get('phone'))
        self.data = {
            'phone': '09199142330',
            'code': code
        }
        response = self.client.post(reverse(self.VERIFY_ENDPOINT), self.data)
        self.assertEqual(response.data, {'phone_verified': True})

    def test_signin_user(self):
        self.data = {
            'phone_or_email': '09199142330',
            'password': '12345678'
        }
        response = self.client.post(reverse(self.SIGNIN_ENDPOINT), self.data)
        self.assertEqual(response.status_code, 201)
