from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.gallery,name='gallery'),
    path('view/<str:pk>/', views.viewphoto,name='view'),
    path('add/', views.add, name='add'),
    path('register/',views.register,name='register'),
    path('admin_portal/',views.admin_portal,name='admin_portal'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)