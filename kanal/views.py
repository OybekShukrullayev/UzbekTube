# from rest_framework.response import Response
# from rest_framework.status import HTTP_204_NO_CONTENT
# from rest_framework.views import APIView
# from .serializers import KanalSerializer
# from .models import Kanal
#
#
# class KanalListCreateAPIView(APIView):
#     def get(self, request):
#         kanal = Kanal.objects.all()
#         serializer = KanalSerializer(kanal, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = KanalSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#
# class KanalDetailAPIView(APIView):
#     def get(self, request, pk):
#         serializer = KanalSerializer(self.get_object(pk))
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         kanal = self.get_object(pk)
#
#         serializer = KanalSerializer(
#             kanal,
#             data=request.data
#         )
#
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(serializer.data)
#
#     def patch(self, request, pk):
#         kanal = self.get_object(pk)
#
#         serializer = KanalSerializer(
#             kanal,
#             data=request.data,
#             partial=True
#         )
#
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(serializer.data)
#
#     def delete(self, request, pk):
#         self.get_object(pk).delete()
#         return Response(status=HTTP_204_NO_CONTENT)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Kanal


@login_required
def kanal_yaratish(request):
    if hasattr(request.user, 'kanal') and request.user.kanal is not None:
        return redirect('kanal_detay')

    if request.method == 'POST':
        nomi = request.POST.get('nomi')
        description = request.POST.get('description')
        identifikator = request.POST.get('identifikator')
        havolalar = request.POST.get('havolalar')

        if Kanal.objects.filter(identifikator=identifikator).exists():
            messages.error(request, 'Bu identifikator allaqachon band.')
            return render(request, 'kanal/kanal_post.html')

        Kanal.objects.create(
            user=request.user,
            nomi=nomi,
            description=description,
            identifikator=identifikator,
            havolalar=havolalar
        )
        messages.success(request, 'Kanal muvaffaqiyatli yaratildi!')
        return redirect('home')

    return render(request, 'kanal/kanal_post.html')


@login_required
def kanal_detay(request):
    kanal = get_object_or_404(Kanal, user=request.user)
    videolar = kanal.videos.all().order_by('-created_at')
    return render(request, 'kanal/kanal_get.html', {'kanal': kanal, 'videolar': videolar})


@login_required
def kanal_tahrirlash(request):
    kanal = get_object_or_404(Kanal, user=request.user)
    if request.method == 'POST':
        kanal.nomi = request.POST.get('nomi')
        kanal.description = request.POST.get('description')
        kanal.havolalar = request.POST.get('havolalar')
        kanal.save()
        messages.success(request, 'Kanal muvaffaqiyatli yangilandi!')
        return redirect('kanal_detay')
    return render(request, 'kanal/kanal_put.html', {'kanal': kanal})


@login_required
def kanal_ochirish(request):
    kanal = get_object_or_404(Kanal, user=request.user)
    if request.method == 'POST':
        kanal.delete()
        messages.success(request, 'Kanal muvaffaqiyatli o\'chirildi!')
        return redirect('home')
    return redirect('kanal_detay')