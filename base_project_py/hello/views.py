from django.shortcuts import render
from django.http import HttpResponse
def homePageView(request):
    return HttpResponse('Hello, World!')
def say_hello(request):
    return render(request, 'hello.html', {'username': 'User' }) # new
