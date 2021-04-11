from django.shortcuts import render

# Create your views here.


class Todo:

    todo_list = []

    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def add_item(self):
        Todo.todo_list.append(self)

    def __str__(self):
        return "Name: " + self.name + ", Priority: "+self.priority

def home(request):
    return  render(request, "todos/home.html")


def list(request):

    name = request.GET.get("name")
    priority = request.GET.get("priority")
    obj = Todo(name, priority)
    obj.add_item()
    return  render(request, "todos/view_todos.html", {"todos": Todo.todo_list})
