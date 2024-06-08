from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import TestSuite
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tests')
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

