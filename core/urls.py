from django.urls import path
from django.conf.urls import handler404

from core.views import home, submit_form, language, success_submit, languageAz
from . import views

urlpatterns = [
    path('', languageAz, name='language'),
    path('home/', home, name='home'),
    path('az/', home, name='az'),
    path('en/', home, name='en'),
    path('submit_form/', submit_form, name='submit_form'),
    path('get_brands/', views.get_brands, name='get_brands'),
    path('success-submit/', success_submit, name='success_submit'),
]

# Custom 404 error handler
handler404 = 'core.views.page_not_found'
