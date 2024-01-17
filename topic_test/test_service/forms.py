from django import forms

class QuestionFormSet(forms.models.BaseInlineFormSet):
    def clean(self):
        correct_array = []
        for data in self.cleaned_data:
            correct_array.append(data['correct'])
            if all(correct_array) or not any(correct_array):
                raise forms.ValidationError('There should be at least one correct option per question and check that not all options are marked as correct')
