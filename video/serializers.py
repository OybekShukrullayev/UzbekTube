from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    channel_name = serializers.CharField(source='user.username', read_only=True)
    channel_avatar = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = [
            'id', 'title', 'description', 'thumbnail', 'video',
            'ochiqligi', 'created_at', 'channel_name', 'channel_avatar'
        ]
        read_only_fields = ['created_at', 'channel_name', 'channel_avatar']

    def get_channel_avatar(self, obj):
        if hasattr(obj.user, 'profile') and obj.user.profile.avatar:
            return obj.user.profile.avatar.url
        return None