from django.urls import reverse

from .base import BaseAPITestCase


class AuthTokenAPIViewTest(BaseAPITestCase):
    def test_get_token(self):
        url = reverse('auth-token')
        payload = {
            'username': 'test-user',
            'password': 'test-pass',
        }
        response = self.client.post(url, payload, format='json')
        assert b'token' in response.content
        assert response.status_code == 200
