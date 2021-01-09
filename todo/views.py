from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_out
from todo.models import Todo
from todo.forms import TaskForm

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

def logout(request):
    auth_out(request)
    return redirect('/login')



def passwordreset(request):
    return render(request, 'todo/passwordreset.html')

def dashboard(request):
    user = request.user
    user_todos = Todo.objects.filter(user=user)
    print(user_todos)

    # {'csrfmiddlewaretoken': ['rMOt8nhJfqtLJzFbGO0a3qDQWGWEJh8RvV1C6jDPgsOZ41JLY8yNkjc8DiHGfqAR'], 'task_name': ['Cook lunch'], 
    # 'task_desc': ['cook rice and stew'], 'status': ['In Progress'], 'priority': ['1'], 'due_date': ['2021-01-20']

    if request.method == "POST":
        print("inside post")
        print(request.POST)
        post_data = request.POST

        task_name= post_data["task_name"]
        task_desc= post_data["task_desc"]
        status= post_data["status"]
        priority= post_data["priority"]
        due_date= post_data["due_date"]

        add_task(user, task_name, task_desc, status, priority, due_date)

    context={
        "user":user,
        "user_todos":user_todos,
    }

    return render(request, 'todo/dashboard.html', context)



#create a function to add task
def add_task(user, task_name, task_desc, status, priority, due_date):
    todo_obj=Todo.objects.create(
        user=user,
        task_name=task_name,
        task_desc=task_desc,
        status=status,
        priority=priority,
        due_date=due_date
    )
    return todo_obj

def task_detail(request, tid):

    todo_obj = Todo.objects.filter(id=tid)

    context={
        "todo_obj": todo_obj,
    }

    return render(request, 'todo/task_detail.html', context)



def task_edit(request, tid):

    todo_obj = Todo.objects.filter(id=tid)
    instance= get_object_or_404(Todo, id=tid)

    form = TaskForm(request.POST or None, instance=instance)

    if request.method == "POST":
        print("****", request.POST)
        post_data = request.POST

        task_name= post_data["task_name"]
        task_desc= post_data["task_desc"]
        status= post_data["status"]
        priority= post_data["priority"]
        due_date= post_data["due_date"]

        Todo.objects.filter(id=tid).update(
            task_name=task_name,
            task_desc=task_desc,
            status=status,
            priority=priority,
            due_date=due_date
        )

        return redirect("/dashboard")
    
    context={
        "todo_obj": todo_obj,
        "form": form,
    }

    return render(request, 'todo/task_edit.html', context)

def task_delete(request, tid):

    todo_obj = Todo.objects.get(id=tid).delete()
    return redirect("/dashboard")