from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from todo.models import Todo

def homepage(request):

    return render(request, 'todo/homepage.html')
    
def register(request):
    print("i have been hit")

    # take data from site
    # store data in database
# {'csrfmiddlewaretoken': ['pZ4N6AKNRGAEu4mS65kL7sd91SzWMDRTE1PbGlIIiILsdXbiYKzsVnHdZF9Ii6jN'], 
# 'username': ['g'], 'email': ['p'], 'password': ['d']}
    if request.method == "POST":
        print("inside post")
        print(request.POST)
        post_data = request.POST
        print("-------",post_data["username"])
        username = post_data["username"]
        email = post_data["email"]
        password = post_data["password"]

        # if len(username)==0:
        user = User.objects.create(
            username = username,
            password=password,
            email=email,
        )

        # if user:
        return redirect('/dashboard')








    return render(request, 'todo/register.html', context={})

def login(request):
    if request.method == "POST":
        print("inside post")
        print(request.POST)
        post_data = request.POST
        print("-------",post_data["username"])
        username = post_data["username"]
        password = post_data["password"]

        # if len(username)==0:
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print("user logged in")
            return redirect('/dashboard')



    return render(request, 'todo/login.html')

def passwordreset(request):
    return render(request, 'todo/passwordreset.html')

def dashboard(request):
    user = request.user

    user_todos = Todo.objects.filter(user=user)

    print(user_todos)

    context={
        "user":user,
        "user_todos":user_todos,
    }
    return render(request, 'todo/dashboard.html', context)

