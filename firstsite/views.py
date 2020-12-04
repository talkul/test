from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('Hello 2F!!!')

def home(request):
    return render(request,'home.html',{'greeting':'Hello'})
    