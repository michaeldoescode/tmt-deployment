# ProTwo/urls.py

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('apptwo/', include('AppTwo.urls')),
    path('', include('AppTwo.urls')),  # Add this line
]

