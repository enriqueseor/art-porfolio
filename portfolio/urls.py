from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # No es necesario usar include() para admin
    path('', include('gallery.urls')),  # Incluye las rutas de la app 'gallery'
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
