from django.db import models

class Kanal(models.Model):
    nomi = models.CharField(max_length=100)
    description = models.TextField()
    identifikator = models.CharField(max_length=50, unique=True)
    havolalar = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nomi
