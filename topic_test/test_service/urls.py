from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('all_tests/', TestListView.as_view(), name='test-list'),
    # path('test/<int:pk>', TestDetailView.as_view(), name='test-detail'),
    # path('result/', TestResultView.as_view(), name='test-result'),
    path('test/<int:test_id>/question/<int:question_index>/', QuestionView.as_view(), name='question-view'),
    path('test/<int:test_id>/result/', TestResultView.as_view(), name='test-result'),
]

