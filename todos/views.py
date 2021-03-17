from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

# Create your views here.

def index(request):

    todos = Todo.objects.order_by('id').reverse()
    return render(request, 'index.html', {'todos' : todos})

def search(request):

    val = request.GET['searchval'].lower()
    if val == 'completed':
        todos = Todo.objects.filter(isCompleted = True)
    elif val == 'unfinished':
        todos = Todo.objects.filter(isCompleted = False)
    else:
        todos = Todo.objects.filter(todo_name__icontains = val)
    return render(request, 'index.html', {'todos': todos})

def addtodo(request):
    val = request.POST['addtodoval']
    valx = Todo(todo_name=val)
    valx.save()
    return redirect('index')

def deletetodo(request):
    val = request.GET['id']
    valx = Todo.objects.get(id=val)
    valx.delete()
    return redirect('index')
    return HttpResponse("Delete Todo")

def edittodo(request):
    val = request.GET['id']
    valx = Todo.objects.get(id=val)
    valx.isCompleted = True
    valx.save()
    return redirect('index')