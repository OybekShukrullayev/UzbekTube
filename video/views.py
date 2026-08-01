from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Video
from kanal.models import Kanal


def home(request):
    # Bosh sahifada barcha ochiq videolar ko'rinadi (update/delete tugmalarisiz)
    videolar = Video.objects.filter(ochiqligi='public').order_by('-created_at')
    return render(request, 'video/video_get.html', {'videolar': videolar, 'my_videos': False})


@login_required
def mening_videolarim(request):
    # Faqat login qilgan userning o'z videolari
    videolar = Video.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'video/video_get.html', {'videolar': videolar, 'my_videos': True})


@login_required
def video_yuklash(request):
    # Faqat kanal yaratgan user video yuklay oladi
    if not Kanal.objects.filter(user=request.user).exists():
        messages.error(request, 'Video yuklash uchun avval kanal yaratishingiz kerak!')
        return redirect('kanal_yaratish')

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        ochiqligi = request.POST.get('ochiqligi', 'public')
        thumbnail = request.FILES.get('thumbnail')
        video_file = request.FILES.get('video')

        if not title or not video_file:
            messages.error(request, 'Video nomi va video fayl majburiy!')
            return render(request, 'video/video_post.html')

        Video.objects.create(
            user=request.user,
            kanal=request.user.kanal,
            title=title,
            description=description,
            ochiqligi=ochiqligi,
            thumbnail=thumbnail,
            video=video_file
        )
        messages.success(request, 'Video muvaffaqiyatli yuklandi!')
        return redirect('mening_videolarim')

    return render(request, 'video/video_post.html')


@login_required
def video_tahrirlash(request, video_id):
    video = get_object_or_404(Video, id=video_id, user=request.user)
    if request.method == 'POST':
        video.title = request.POST.get('title')
        video.description = request.POST.get('description')
        video.ochiqligi = request.POST.get('ochiqligi', video.ochiqligi)
        if request.FILES.get('thumbnail'):
            video.thumbnail = request.FILES.get('thumbnail')
        if request.FILES.get('video'):
            video.video = request.FILES.get('video')
        video.save()
        messages.success(request, 'Video muvaffaqiyatli yangilandi!')
        return redirect('mening_videolarim')
    return render(request, 'video/video_put.html', {'video': video})


@login_required
def video_ochirish(request, video_id):
    video = get_object_or_404(Video, id=video_id, user=request.user)
    if request.method == 'POST':
        video.delete()
        messages.success(request, 'Video muvaffaqiyatli o\'chirildi!')
    return redirect('mening_videolarim')