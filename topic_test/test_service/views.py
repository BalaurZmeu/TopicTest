from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import TestSuite
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from .models import TestSuite, Question, Answer

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('test_list')
    else:
        form = UserCreationForm()
    return render(request, 'test_service/user_register.html', {'form': form })
    
class TestListView(LoginRequiredMixin, generic.ListView):
    model = TestSuite
    template_name = 'test_service/test_list.html'
    paginate_by = 10
    
    def get_queryset(self):
        return (
            TestSuite.objects.all()
        )

# class TestDetailView(LoginRequiredMixin, generic.DetailView):
#    model = TestSuite
#    template_name = 'test_service/test_detail.html'

# class TestResultView(LoginRequiredMixin, generic.ListView):
#    model = TestSuite
#    template_name = 'test_service/test_result.html'

class QuestionView(LoginRequiredMixin, generic.View):
    def get(self, request, test_id, question_index):
        test = get_object_or_404(TestSuite, id=test_id)
        questions = test.get_questions()
        question = questions[question_index]
        return render(request, 'test_service/question.html', {'question': question, 'index': question_index + 1, 'total': questions.count()})

    def post(self, request, test_id, question_index):
        selected_answer_id = request.POST.get('answer')
        if not selected_answer_id:
            return redirect('question-view', test_id=test_id, question_index=question_index)
        
        selected_answer = get_object_or_404(Answer, id=selected_answer_id)
        request.session[f'answer_{question_index}'] = selected_answer.is_correct

        next_index = question_index + 1
        test = get_object_or_404(TestSuite, id=test_id)
        if next_index < test.get_questions().count():
            return redirect('question-view', test_id=test_id, question_index=next_index)
        else:
            return redirect('test-result', test_id=test_id)

class TestResultView(LoginRequiredMixin, generic.View):
    def get(self, request, test_id):
        test = get_object_or_404(TestSuite, id=test_id)
        questions = test.get_questions()
        total = questions.count()
        correct = sum(1 for i in range(total) if request.session.get(f'answer_{i}', False))
        return render(request, 'test_service/result.html', {'correct': correct, 'total': total, 'percentage': (correct / total) * 100})

