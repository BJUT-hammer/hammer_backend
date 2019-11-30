import json

from django.db.models import ProtectedError
from rest_framework import viewsets
from rest_framework import pagination
from rest_framework import permissions
from rest_framework.views import APIView

from hammer_api.exceptions import BaseError
from hammer_api.api.authentication import ExpiringTokenAuthentication


class BasePageNumberPagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class BaseModelViewSet(viewsets.ModelViewSet):
    pagination_class = BasePageNumberPagination


class BaseReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class = BasePageNumberPagination


class BaseAPIView(APIView):
    pass
