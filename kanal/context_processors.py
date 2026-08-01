from .models import Kanal

def user_kanal_context(request):
    if request.user.is_authenticated:
        has_kanal = Kanal.objects.filter(user=request.user).exists()
        try:
            user_kanal = request.user.kanal
        except Kanal.DoesNotExist:
            user_kanal = None
        return {'has_kanal': has_kanal, 'user_kanal': user_kanal}
    return {'has_kanal': False, 'user_kanal': None}