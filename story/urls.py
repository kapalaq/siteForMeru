from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import home

urlpatterns = [
    path('home/', home, name="home")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
