from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    
def tests(request):
    return render(request, 'test_service/test_list.html')
