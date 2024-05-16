from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

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
    
def tests(request):
    return render(request, 'test_service/test_list.html')

