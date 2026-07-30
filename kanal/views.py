from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from .serializers import KanalSerializer
from .models import Kanal


class KanalListCreateAPIView(APIView):
    def get(self, request):
        kanal = Kanal.objects.filter()
        serializer = KanalSerializer(kanal, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = KanalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class KanalDetailAPIView(APIView):
    def get(self, request, pk):
        serializer = KanalSerializer(self.get_object(pk))
        return Response(serializer.data)

    # def put(self, request, pk):
    #     serializer = KanalSerializer(pk=pk)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    #
    # def patch(self, request, pk):
    #     serializer = KanalSerializer(self.get_object(pk), data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

    def put(self, request, pk):
        kanal = self.get_object(pk)

        serializer = KanalSerializer(
            kanal,
            data=request.data
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def patch(self, request, pk):
        kanal = self.get_object(pk)

        serializer = KanalSerializer(
            kanal,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)
