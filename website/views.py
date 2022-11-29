from django.shortcuts import render

def request(request):
    
    return render(request,'request.html')

def home(request):
    return render(request,'welcome.html')