from django.contrib import admin
from django.urls import path, include

from mywebsite import settings
from . import views

from django.conf import settings # 
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('blog/', include('blog.urls')),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
    path('projects/', include('projects.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)