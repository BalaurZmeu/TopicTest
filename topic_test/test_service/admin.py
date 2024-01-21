from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from test_service.models import *

class AnswerInline(NestedStackedInline):
    model = Answer
    fk_name = 'level'
    extra = 0

class QuestionInline(NestedStackedInline):
    model = Question
    fk_name = 'level'
    extra = 0
    inlines = [AnswerInline]

class TestSuiteAdmin(NestedModelAdmin):
    model = TestSuite
    inlines = [QuestionInline]


admin.site.register(TestSuite, TestSuiteAdmin)

