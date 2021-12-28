from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect
# from django.urls import reverse
from .models import Task
from .forms import TaskForm, UpdateTaskForm

# Create your views here.


def show_all_task(request):
    all_task = Task.objects.order_by('is_complete', 'due')
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()     # save all data in model contained in the form
        return redirect('/')
    else:
        form = TaskForm()
    return render(request, 'todo/show_all_task.html', {'all_task': all_task, 'form': form})


def update_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = UpdateTaskForm(instance=task)
    return render(request, 'todo/update_task.html', {'form': form})


def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'todo/delete_task.html', {'task': task})
