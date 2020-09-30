from django.db import models
from django.utils import timezone


class Tags(models.Model):

    id = models.BigAutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=16, verbose_name='タグ名')
    color = models.CharField(max_length=7, verbose_name='カラーコード')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 't_tags'
