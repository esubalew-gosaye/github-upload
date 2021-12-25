"""
    test2 URL Configuration
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Photo_Gallery.urls'))
]
