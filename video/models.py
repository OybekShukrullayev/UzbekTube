from django.db import models

class Video(models.Model):
    thumbnail = models.ImageField(upload_to='thumbnail/', null=True, blank=True)
    video = models.FileField(upload_to='video/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Ochiqligi(models.Model):
        OCHIQLIGI_CHOICES = [
            ('Open to everyone', 'Hammaga ochiq'),
            ('Via link', 'Havola orqali'),
            ('Confidential', 'Maxfiy')
        ]