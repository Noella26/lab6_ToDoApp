from django.shortcuts import render
from .models import TodoListItem 
from django.http import HttpResponseRedirect 
# Create your views here.
def index(request):
    return render(request, 'index.html')



def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',  {'all_items':all_todo_items})


def addTodoView(request):
    new_item = TodoListItem()
    new_item.content = request.POST.get('content')
    new_item.save()
    return HttpResponseRedirect('/todo/') 


def deleteTodoView(request, id):
    y = TodoListItem.objects.get(id= id)
    y.delete()
    return HttpResponseRedirect('/todo/') 

def updateTodoView(request, id):
    x= TodoListItem.objects.get(id= id)
    if request.method == "POST":
        content = request.POST.get('updated_content')
        x.content = content
        x.save()
        return HttpResponseRedirect('/todo/')