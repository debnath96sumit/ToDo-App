from django.http import HttpResponse
from django.shortcuts import redirect, render
from home.models import Task

# Create your views here.
def home(request):
    context = {'success' : False}
    if request.method == "POST":

        title = request.POST['title']
        desc = request.POST['desc']
        # print(title, desc)

        ins  = Task(taskTitle = title, taskDesc = desc)
        ins.save()
        context = {'success' : True}
    return render(request, 'index.html', context)

def tasks(request):
    alltasks = Task.objects.all()
    context = {'tasks': alltasks}
    return render(request, 'tasks.html', context)

def delete(request, id):
    instance = Task.objects.get(id=id)
    instance.delete()
    return redirect('/tasks')

def search(request):
    query = request.GET['query']
    alltasks = Task.objects.filter(taskTitle__icontains =query)
    context = {'tasks': alltasks}
    return render(request, 'search.html', context)

       
