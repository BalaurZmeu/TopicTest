from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('test_service.urls')),  # Include the app-specific URLs
    # Other project-wide URL patterns go here
]
