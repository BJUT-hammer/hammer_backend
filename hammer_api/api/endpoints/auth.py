from logging import getLogger

from django.http import JsonResponse
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token

from .base import BaseAPIView
from ..serializers import AuthSerializer, UserSerializer
from ..authentication import get_token_expires, is_token_expired


logger = getLogger('hammer_api')


class AuthTokenAPIView(BaseAPIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        """获取用户 token, 使用 用户名和密码。

        request data: {"username": "user", "password": "pass"}

        response data:

        {
            "token": "abcddemo",
            "expires": "2013-01-29T12:34:56.000000Z"     # 过期时间，ISO 8601 格式
        }

        然后使用如下 HTTP Header:

        ```
         Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
        ```

        测试环境账号：admin/admin123
        """
        auth_serializer = AuthSerializer(data=request.data)
        if not auth_serializer.is_valid():
            return JsonResponse(auth_serializer.errors, status=400)
        username = auth_serializer.validated_data['username']
        password = auth_serializer.validated_data['password']
        user = authenticate(username=username, password=password)
        if user is None:
            raise AuthenticationFailed()
        token, _ = Token.objects.get_or_create(user=user)
        if is_token_expired(token):
            token.delete()
            token, _ = Token.objects.get_or_create(user=user)
        user_serialized = UserSerializer(user)
        data = {
            'token': token.key,
            'expires': get_token_expires(token),
            'user': user_serialized.data,
        }
        return JsonResponse(data)
