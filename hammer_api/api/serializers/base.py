from rest_framework import serializers


class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ()
        depth = 0
