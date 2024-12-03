from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static
from StatTrackr.views import get_csrf_token

urlpatterns = [
    path('api/auth/csrf/', get_csrf_token),
    path('admin/', admin.site.urls),
    path('api/', include('StatTrackr.urls')),  # Include all StatTrackr URLs under /api/
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', RedirectView.as_view(url='/api/dashboard/')),  # Redirect root to the dashboard
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)