from .models import Kanal
from rest_framework import serializers

class KanalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kanal
        fields = ['nomi', 'description', 'identifikator', 'havolalar']