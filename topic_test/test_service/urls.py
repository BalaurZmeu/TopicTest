from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('tests/', TestListView.as_view(), name='tests'),
    path('testing/', TestDetailView.as_view(), name='testing'),
    path('result/', TestResultView.as_view(), name='result'),
]
