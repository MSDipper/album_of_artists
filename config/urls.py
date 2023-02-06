from django.contrib import admin
from django.urls import path, include 
from config.yasg import urlpatterns as doc_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('album.urls')),
    
]
urlpatterns += doc_urls