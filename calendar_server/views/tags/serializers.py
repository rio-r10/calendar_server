from rest_framework import serializers
from calendar_server.models import Tags


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class TagRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=16)
    color = serializers.CharField(max_length=7, min_length=7)

