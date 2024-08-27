from django.shortcuts import render, redirect
from .models import Todo
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def home(request):
    if request.method == 'POST':
        my_title = request.POST.get('title')
        my_desc = request.POST.get('desc')

        todo = Todo.objects.create(title=my_title, description=my_desc)
        todo.save()

        redirect('/')

    todos = Todo.objects.all()

    return render(request, 'index.html', {'todos':todos})



def deleteTodo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('home')