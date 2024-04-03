# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Register
from .forms import RegisterForm

def register_list(request):
    registers = Register.objects.all()
    return render(request, 'register_list.html', {'registers': registers})

def register_create(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_list')
    else:
        form = RegisterForm()
    return render(request, 'register_form.html', {'form': form})

def register_update(request, pk):
    register = get_object_or_404(Register, pk=pk)
    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=register)
        if form.is_valid():
            form.save()
            return redirect('register_list')
    else:
        form = RegisterForm(instance=register)
    return render(request, 'register_form.html', {'form': form})

def register_delete(request, pk):
    register = get_object_or_404(Register, pk=pk)
    if request.method == 'POST':
        register.delete()
        return redirect('register_list')
    return render(request, 'register_confirm_delete.html', {'register': register})
