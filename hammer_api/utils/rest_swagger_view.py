from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView
from rest_framework_swagger import renderers
from django.contrib.auth.models import User


class SwaggerSchemaView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]

    def get(self, request):
        generator = SchemaGenerator(title='Base API')
        try:
            user = User.objects.get(username='hammer-api-swagger-bot')
        except User.DoesNotExist:
            user = User.objects.create(username='hammer-api-swagger-bot')
        request.user = user
        request.auth = (user, None)
        schema = generator.get_schema(request)

        return Response(schema)
