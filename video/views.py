from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Video
from .serializers import VideoSerializer
from rest_framework.status import HTTP_204_NO_CONTENT

class VideoListCreateAPIView(APIView):
    def get(self, request):
        video = Video.objects.all()
        serializer = VideoSerializer(video, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = VideoSerializer(many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class VideoDetailAPIView(APIView):
    def get_detail(self, request, id):
        serializer = VideoSerializer(self.get_object(id))
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = VideoSerializer(self.get_object(pk), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk):
        serializer = VideoSerializer(self.get_object(pk), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)
