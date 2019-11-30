from logging import getLogger

from django.http import JsonResponse

from .base import BaseAPIView
from ..serializers import UserSerializer
from ..authentication import get_token_expires


logger = getLogger('hammer_api')


class MeAPIView(BaseAPIView):
    def get(self, request):
        """获取当前登录用户信息。

        response data:
        {
            "user": {"username": "user"},
            "expires": "2013-01-29T12:34:56.000000Z", # 过期时间，ISO 8601 格式
        }
        """
        user_serialized = UserSerializer(request.user)
        data = {
            'expires': get_token_expires(request.auth),
            'user': user_serialized.data,
        }
        return JsonResponse(data)
