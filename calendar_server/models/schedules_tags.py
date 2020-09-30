from django.db import models
from calendar_server.models import Schedules, Tags


class SchedulesTags(models.Model):

    id = models.BigAutoField(unique=True, primary_key=True)
    schedule_id = models.ForeignKey(
        Schedules, on_delete=models.CASCADE, related_name='schedule_tags', verbose_name='スケジュール'
    )
    tag_id = models.ForeignKey(Tags, on_delete=models.CASCADE, related_name='tag_schedules', verbose_name='タグ')

    class Meta:
        db_table = 'r_schedules_tags'
