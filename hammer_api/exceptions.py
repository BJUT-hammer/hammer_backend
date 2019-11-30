# -*- coding: utf-8 -*-
from rest_framework.views import exception_handler
from django.http import JsonResponse


class BaseError(Exception):
    pass


def hammer_api_error_handler(exc, context):
    if isinstance(exc, BaseError):
        response = JsonResponse(dict(errors={'non_field_errors': [unicode(exc)]}), status=400)
    else:
        response = exception_handler(exc, context)
    return response
