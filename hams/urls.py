from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('family/', include('family.urls')),
    path('', include('family.urls')),
    path('users/', include('users.urls')),
    path('wordcount/', include('wordcount.urls'), name='wordcount'),
    path('blog/', include('blog.urls')),
    path('jobs/', include('jobs.urls')),
    path('portfolio/', include('jobs.urls')),
    path('email/', include('emailsending.urls')),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # This line is for showing images and files to the client via url
