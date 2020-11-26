from django.http.response import HttpResponse
from django.shortcuts import render,redirect

from datetime import datetime
# from django.http import HttpResponse

from .forms import *

from .models import *
# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form  = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks' : tasks, 'form' : form}
    return render(request, 'todolist/list.html', context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)
    task.deleted = datetime.now()
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance = task)
        
        if form.is_valid():
            
            form.save()
            return redirect('/')

    context = {'form' : form}
    return render(request, 'todolist/update_task.html',context)
 


def deleteTasks(request, pk):
    item = Task.objects.get(id=pk)
    
    if request.method == "POST":
        item.delete()
        return redirect('/')

    # context = {'item' : item}
    # return render(request,'todolist/delete.html', context)
