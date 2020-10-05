from rest_framework import serializers
from calendar_server.models import Schedules, SchedulesTags
from calendar_server.views.tags.serializers import TagSerializer


class SchedulesTagsSerializer(serializers.ModelSerializer):
    tag = TagSerializer()

    class Meta:
        model = SchedulesTags
        fields = '__all__'


class SchedulesSerializer(serializers.ModelSerializer):
    tags = SchedulesTagsSerializer(many=True)

    class Meta:
        model = Schedules
        fields = '__all__'


class ScheduleRequestSerializer(serializers.Serializer):
    text = serializers.CharField()
    date = serializers.CharField(max_length=10, min_length=10)
    tags = serializers.ListField(
        child=serializers.IntegerField()
    )
