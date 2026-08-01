from django.db import models
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Video(models.Model):
    OCHIQLIGI_CHOICES = [
        ('public', 'Hammaga ochiq'),
        ('unlisted', 'Havola orqali'),
        ('private', 'Maxfiy')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='videos')
    kanal = models.ForeignKey('kanal.Kanal', on_delete=models.CASCADE, related_name='videos', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    video = models.FileField(upload_to='videos/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    ochiqligi = models.CharField(max_length=20, choices=OCHIQLIGI_CHOICES, default='public')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title