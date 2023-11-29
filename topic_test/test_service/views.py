from django.shortcuts import render

def welcome(request):
    return render(request, 'test_service/welcome.html')
