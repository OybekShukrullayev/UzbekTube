from .models import Video
from rest_framework import serializers

class VideoSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Video
        fields = ['id', 'user', 'thumbnail', 'video', 'title', 'description', 'ochiqligi', 'created_at']
        read_only_fields = ['user', 'created_at']