from django.shortcuts import render
from .models import Todo
from django.template import RequestContext
# Create your views here.

def finish_todo(request):
    todo = Todo.objects.get(title=request.GET.get('title'))
    todo.status = "Finished"
    todo.save()

    todos = Todo.objects.all().order_by('-due_date')
    return render(request, "todos/view_todos.html", {"todos": todos})

def edit_todo(request):
    print(request.GET.get('title'))
    pass

def delete_todo(request):
    todo = Todo.objects.filter(title=request.GET.get('title')).delete()
    todos = Todo.objects.all().order_by('-due_date')
    return render(request, "todos/view_todos.html", {"todos": todos})


def view_todos(request):

    if request.POST.get('title') != None:

        todo = Todo()
        todo.title = request.POST.get('title')
        todo.notes = request.POST.get('notes')
        todo.due_date = request.POST.get('date')
        todo.priority = request.POST.get('priority')
        todo.save()

    todos = Todo.objects.all().order_by('-due_date')

    return  render(request, "todos/view_todos.html",{"todos": todos})

def add_todo(request):

    return render(request, "todos/add_todo.html")
