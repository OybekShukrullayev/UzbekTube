from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Video
from .serializers import VideoSerializer
from rest_framework.status import HTTP_204_NO_CONTENT

class VideoListCreateAPIView(APIView):
    # def get(self, request):
    #     video = Video.objects.all()
    #     serializer = VideoSerializer(video, many=True)
    #     return Response(serializer.data)

    def get(self, request):
        videos = Video.objects.filter(ochiqligi='public').order_by('-created_at')
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)

    # def post(self, request, *args, **kwargs):
    #     serializer = VideoSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=1)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VideoDetailAPIView(APIView):
    # def get_detail(self, request, id):
    #     serializer = VideoSerializer(self.get_object(id))
    #     return Response(serializer.data)

    def get_detail(self, request, id):
        video = Video.objects.get(id=id)
        serializer = VideoSerializer(video)
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


# class HomeVideoListAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         videos = Video.objects.filter(ochiqligi='public').order_by('-created_at')
#         serializer = VideoSerializer(videos, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
# class MyVideoListAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         videos = Video.objects.filter(user=request.user).order_by('-created_at')
#         serializer = VideoSerializer(videos, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)