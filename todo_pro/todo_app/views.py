from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoItemForm
def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo_app/todo_list.html', {'todos': todos})

def todo_create(request):
    form = TodoItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('todo_list')
    return render(request, 'todo_app/todo_form.html', {'form': form})

def todo_update(request, id):
    todo = TodoItem.objects.get(id=id)
    form = TodoItemForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('todo_list')
    return render(request, 'todo_app/todo_form.html', {'form': form, 'todo': todo})

def todo_delete(request, id):
    todo = TodoItem.objects.get(id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo_app/todo_delete_confirm.html', {'todo': todo})
