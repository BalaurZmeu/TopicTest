from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('tests/', TestListView.as_view(), name='tests'),
    path('register/', register, name='register'),
]
