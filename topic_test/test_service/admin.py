from django.contrib import admin
from django import forms
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from test_service.models import *

class AnswerModelForm(forms.models.BaseInlineFormSet):
    class Meta:
        model = Answer
        fields = "__all__"
        
    def clean(self):
        true_answer_count = 0
        answer_count = 0
        for form in self.forms:
            try:
                if form.cleaned_data.get("is_correct") is True:
                    true_answer_count += 1
                answer_count += 1
            except AttributeError:
                pass
        if true_answer_count == 0:
            raise forms.ValidationError(
                ("A question must have at least one correct answer.")
            )
        if true_answer_count == answer_count:
            raise forms.ValidationError(
                ("Not all answers can be correct.")
            )

class AnswerInline(NestedStackedInline):
    formset = AnswerModelForm
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

