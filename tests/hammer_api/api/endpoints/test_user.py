from django.urls import reverse

from .base import BaseAPITestCase


class MeAPIViewTest(BaseAPITestCase):
    def test_get_me(self):
        url = reverse('me')
        response = self.client.get(url)
        assert response.status_code == 200
