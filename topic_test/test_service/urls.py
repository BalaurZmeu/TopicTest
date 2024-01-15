from django.urls import path
from .views import *

urlpatterns = [
    path('', welcome, name='welcome'),
    path('tests', tests, name='tests'),
]
