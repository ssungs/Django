from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import TodoList

# Create your views here.

def index(request):
    todo_lists = TodoList.objects.all()

    content = {
        'todo_lists': todo_lists
    }
    print(HttpResponse(request))
    return render(request, 'index.html', content)

def add(request):
    print(request.method)
    print(request.POST['todolist'])
    if request.method == 'POST':
        todolist = request.POST['todolist']

        todo_list = TodoList.objects.create(
            todolist=todolist,
        )

        return redirect('index')
    print(todo_list)

    return render(request, 'index.html')

def edit(request, todo_list_pk):

    return redirect('edit')

def complete(request, todo_list_pk):
    return render(request, 'index.html')

def delete(request, todo_list_pk):
    return render(request, 'index.html')