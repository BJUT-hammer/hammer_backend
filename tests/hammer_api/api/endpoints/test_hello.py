from django.urls import reverse

from .base import BaseAPITestCase


class HelloAPIViewTest(BaseAPITestCase):
    def test_hello(self):
        url = reverse('hello-username')
        request_data = {
            'username': 'test-user',
        }
        response = self.client.post(url, request_data, format='json')
        assert b'hello test-user' in response.content
        assert response.status_code == 200
