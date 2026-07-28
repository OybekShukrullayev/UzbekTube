from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import KanalSerializer
from .models import Kanal

class KanalListCreateAPIView(APIView):
    def get(self, request):
        kanal = Kanal.objects.filter()
        serializer = KanalSerializer(kanal, many=True)
        return Response(serializer.data)

    def post(self):
        pass