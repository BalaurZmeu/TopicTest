from django.contrib import admin

from .forms import QuestionFormSet
from .models import TestSuite, Question, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    formset = QuestionFormSet
    min_num = 3
    max_num = 5
    extra = 1

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

@admin.register(TestSuite)
class TestSuiteAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_filter = ['test_suite']
