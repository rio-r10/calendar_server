from rest_framework import serializers
from calendar_server.models import Schedules, SchedulesTags, Tags


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class SchedulesTagsSerializer(serializers.ModelSerializer):
    tag_id = TagSerializer()

    class Meta:
        model = SchedulesTags
        fields = '__all__'


class SchedulesSerializer(serializers.ModelSerializer):
    tags = SchedulesTagsSerializer(many=True)

    class Meta:
        model = Schedules
        fields = '__all__'
