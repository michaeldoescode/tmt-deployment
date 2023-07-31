# images/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('help/', views.help, name='help'),  # new URL pattern for the help view
]
