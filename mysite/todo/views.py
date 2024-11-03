from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        Todo.objects.create(task=task)
        return redirect('index')
    return render(request, 'todo/add_todo.html')

def mark_complete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')
