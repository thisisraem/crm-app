from core.models import Settings

def settings(request):
    context = {
        'settings': Settings.objects.first()
    }
    return context