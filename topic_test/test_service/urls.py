from django.urls import path
from .views import welcome

urlpatterns = [
    path('', welcome, name='welcome'),
    # Other app-specific URL patterns go here
]
