from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class BaseAPITestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        # the user
        try:
            user = User.objects.get(username='test-user')
        except User.DoesNotExist:
            user = User.objects.create(username='test-user')
            user.set_password('test-pass')
            user.save()
        token, created = Token.objects.get_or_create(user=user)
        cls.token = token
        super(BaseAPITestCase, cls).setUpClass()

    def setUp(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        super(BaseAPITestCase, self).setUp()
