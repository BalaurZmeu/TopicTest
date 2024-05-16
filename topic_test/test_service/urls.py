from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('tests/', tests, name='tests'),
    path('register/', register, name='register'),
]
