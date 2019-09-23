from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('family/', include('family.urls')),
    path('', include('family.urls')),
    path('users/', include('users.urls')),
    path('wordcount/', include('wordcount.urls'), name='wordcount')

]
