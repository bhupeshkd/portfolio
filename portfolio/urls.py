from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  
from main.views import custom_404

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
] 

handler404 = 'main.views.custom_404'

# Static & Media serving setup for production / Vercel fallback
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )