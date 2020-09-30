from django.db import models
from django.utils import timezone


class Schedules(models.Model):

    id = models.BigAutoField(unique=True, primary_key=True)
    text = models.TextField(null=True, verbose_name='内容')
    date = models.DateField(verbose_name='日程')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 't_schedules'
