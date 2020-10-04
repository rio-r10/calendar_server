from django.db.models import Prefetch
from rest_framework.views import APIView
from rest_framework.response import Response
from dateutil.relativedelta import relativedelta
import datetime
from rest_framework.status import (
    HTTP_200_OK,
)
from calendar_server.models import Schedules, SchedulesTags
from calendar_server.views.schedules.serializers import SchedulesSerializer


class SchedulesViews(APIView):

    def get(self, request):
        year = request.query_params.get('year', None)
        month = request.query_params.get('month', None)
        start_date = datetime.datetime.strptime("{0}-{1}-01".format(year, month), "%Y-%m-%d")
        end_date = start_date + relativedelta(months=1)

        prefetch_tags = Prefetch(
            'schedule_tags',
            SchedulesTags.objects.all().select_related('tag_id'),
            'tags'
        )
        schedules = Schedules.objects.filter(date__gte=start_date, date__lt=end_date, deleted_at=None).prefetch_related(prefetch_tags)
        serializer = SchedulesSerializer(schedules, many=True)

        return Response(status=HTTP_200_OK, data=serializer.data)
