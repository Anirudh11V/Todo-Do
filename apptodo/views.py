from django.shortcuts import render, redirect

from .models import todotask
from .forms import taskForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def logout_user(request):
    logout(request)
    messages.success(request, 'logged out')
    return redirect('hpage')

@login_required
def home(request):
    
    form = taskForm()
    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            msg=form.save(commit=False)
            msg.save()
        
    msg = todotask.objects.all()
    context = {"form": form, "task": msg}

    return render(request, 'apptodo/home.html', context)

def authView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hpage')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def Edit(request,pk):
    todo = todotask.objects.get(id=pk)
    form = taskForm(instance=todo)
    if request.method == 'POST':
        form = taskForm(request.POST, request.FILES, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('hpage')
    return render(request, 'apptodo/edit.html', {"form": form})


def delete(request,pk):
    todo = todotask.objects.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('hpage')
    
    return render(request, 'apptodo/del.html', {"obj": todo})