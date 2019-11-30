from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    pass
    # username = serializers.CharField(required=True, allow_blank=False, max_length=100)
