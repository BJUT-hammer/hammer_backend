# -*- coding: utf-8 -*-
from django.urls import path, include
from rest_framework import routers
from django.conf import settings

from .endpoints.auth import AuthTokenAPIView
from .endpoints.user import MeAPIView
from .endpoints.hello import HelloAPIView


urlpatterns = [
    # path('auth/token/', AuthTokenAPIView.as_view(), name='auth-token'),
    # path('me/', MeAPIView.as_view(), name='me'),
    # hello
    path('hello/', HelloAPIView.as_view(), name='hello-username'),
]
