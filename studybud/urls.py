from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls'))
]
print(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))

# Project URLS
# Project-level URLs handle routing requests on a broader scope, like views for the admin page or between applications. 
# They are defined in the urls.py file located in the project's root directory, next to settings.py
