from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('blog/', include('blog.urls')),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
    path('projects/', include('projects.urls')),
]
