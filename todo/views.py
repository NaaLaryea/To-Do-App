from django.shortcuts import render

def homepage(request):

    return render(request, 'todo/homepage.html')
    
def register(request):
    return render(request, 'todo/register.html')

def login(request):
    return render(request, 'todo/login.html')

def passwordreset(request):
    return render(request, 'todo/passwordreset.html')