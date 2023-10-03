from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls.i18n import i18n_patterns
from rosetta.urls import urlpatterns as rosetta_urls

from core.urls import urlpatterns as core_urls

urlpatterns = [
    path('fashmin/', admin.site.urls),
    path('tatiko/', include(rosetta_urls)), 
    path('', include(core_urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += i18n_patterns(
    # path('', include(core_urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = 'core.views.handling_404'