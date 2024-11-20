from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .drf_yasg import urlpatterns as urls_swagger

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/', include('app.main.urls')),
                  path('api/v1/chat/', include('app.chat_ai.urls')),
                  # path('register/', RegisterAPIView.as_view(), name='register'),
                  # path('login/', LoginAPIView.as_view(), name='login'),
                  path('api/v1/user/', include('rest_framework.urls')),

                  # path('auth/', include('djoser.urls')),
                  # path('auth/', include('djoser.urls.authtoken')),

              ] + urls_swagger
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
