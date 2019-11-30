from django.contrib.auth.models import User

from .base import BaseModelSerializer


class UserSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = User
        fields = ('id', 'username', 'email')
