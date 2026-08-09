from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static  
from main.views import custom_404

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    re_path(r'^(?!static/).*$', custom_404, name='catch_all_404'),
] 


handler404 = 'main.views.custom_404'

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
