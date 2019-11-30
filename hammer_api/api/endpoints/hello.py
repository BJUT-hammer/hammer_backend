from django.http import JsonResponse

from .base import BaseAPIView
from ..serializers import HelloSerializer


class HelloAPIView(BaseAPIView):
    def get(self, request):
        hello_serializer = HelloSerializer(data=request.data)
        if not hello_serializer.is_valid():
            return JsonResponse(hello_serializer.errors, status=400)
        # username = hello_serializer.validated_data['username']
        message = 'hello world' # % username
        data = {
            'message': message,
        }
        return JsonResponse(data)
