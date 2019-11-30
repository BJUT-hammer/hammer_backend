from datetime import timedelta

from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from django.utils import timezone
from django.conf import settings


class ExpiringTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            raise AuthenticationFailed("Invalid Token")
        if not token.user.is_active:
            raise AuthenticationFailed("User is not active")
        if is_token_expired(token):
            raise AuthenticationFailed("The Token is expired")
        return (token.user, token)


def is_token_expired(token):
    time_elapsed = timezone.now() - token.created
    return time_elapsed > timedelta(seconds=settings.AUTH_TOKEN_MAX_AGE)


def get_token_expires(token):
    expires_time = token.created + timedelta(seconds=settings.AUTH_TOKEN_MAX_AGE)
    expires_time = expires_time.isoformat()
    if expires_time.endswith('+00:00'):
        expires_time = expires_time[:-6] + 'Z'
    return expires_time
