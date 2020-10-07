from rest_framework.views import APIView
from django.utils import timezone
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST
)
from calendar_server.views.tags.serializers import TagSerializer, TagRequestSerializer
from calendar_server.models import Tags


class TagsViews(APIView):

    def get(self, request):
        tags = Tags.objects.filter(deleted_at=None)
        serializer = TagSerializer(tags, many=True)

        return Response(status=HTTP_200_OK, data=serializer.data)

    def post(self, request):
        request_serializer = TagRequestSerializer(data=request.data)

        if not request_serializer.is_valid():
            return Response(status=HTTP_400_BAD_REQUEST, data={'errors': ['パラメータが不正です']})

        tag = Tags(
            name=request_serializer.data['name'],
            color=request_serializer.data['color'],
        )

        tag.save()

        return Response(status=HTTP_201_CREATED, data='作成しました')


class TagViews(APIView):
    def delete(self, request, id):
        # スケジュールが存在するか確認
        tag = get_object_or_404(Tags, id=id)

        tag.deleted_at = timezone.now()
        tag.save()

        return Response(status=HTTP_204_NO_CONTENT, data='削除しました')
