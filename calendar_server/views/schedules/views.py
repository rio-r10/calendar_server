from django.db.models import Prefetch
from rest_framework.views import APIView
from rest_framework.response import Response
from dateutil.relativedelta import relativedelta
import datetime
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
)
from calendar_server.models import Schedules, SchedulesTags, Tags
from calendar_server.views.schedules.serializers import SchedulesSerializer, ScheduleRequestSerializer


class SchedulesViews(APIView):

    def get(self, request):
        year = request.query_params.get('year', None)
        month = request.query_params.get('month', None)
        start_date = datetime.datetime.strptime("{0}-{1}-01".format(year, month), "%Y-%m-%d")
        end_date = start_date + relativedelta(months=1)

        prefetch_tags = Prefetch(
            'schedule_tags',
            SchedulesTags.objects.all().select_related('tag'),
            'tags'
        )
        schedules = Schedules.objects.filter(date__gte=start_date, date__lt=end_date, deleted_at=None).prefetch_related(prefetch_tags)
        serializer = SchedulesSerializer(schedules, many=True)

        return Response(status=HTTP_200_OK, data=serializer.data)


class ScheduleViews(APIView):

    def post(self, request):
        request_serializer = ScheduleRequestSerializer(data=request.data)

        if not request_serializer.is_valid():
            return Response(status=HTTP_400_BAD_REQUEST, data={'errors': ['パラメータが不正です']})

        # tagが存在することを確認
        tag_id_list = request_serializer.data['tags']
        tags = Tags.objects.filter(id__in=tag_id_list)
        if len(tag_id_list) != len(tags):
            return Response(status=HTTP_400_BAD_REQUEST, data={'errors': ['パラメータが不正です']})

        schedule = Schedules(
            text=request_serializer.data['text'],
            date=request_serializer.data['date'],
        )

        schedule.save()

        schedule_tags = []
        for tag in tags:
            schedule_tags.append(
                SchedulesTags(
                    schedule=schedule,
                    tag=tag,
                )
            )
        SchedulesTags.objects.bulk_create(schedule_tags)

        return Response(status=HTTP_201_CREATED, data='作成しました')
