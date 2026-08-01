from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Kanal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='kanal', null=True, blank=True)
    nomi = models.CharField(max_length=100)
    description = models.TextField()
    identifikator = models.CharField(max_length=50, unique=True)
    havolalar = models.URLField(null=True, blank=True)
    # created_at ni vaqtincha o'chiring yoki default qo'shing
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nomi