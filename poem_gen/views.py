#from django.contrib.auth import authenticate, login, logout
import random

from django.contrib import messages
from django.shortcuts import redirect, render

from poem_gen.models import CustomUser, Line
from poem_gen.forms import (CustomUserCreationForm, GeneratePoemForm, 
                            WriteLineForm)

def index(request):
    if request.user is not None:
        user = request.user

    menu_prompt = 'so, whatchu tryna do?'
    menu_options = ['generate a poem', 'write a line', 'view notebook']
    context = { 'prompt': menu_prompt, 'items': menu_options, 'user': user }
    return render(request, 'poem_gen/index.html', context)

def get_poem(request):
    chars = []
    lines = []

    if request.method == 'GET':
        form = GeneratePoemForm(request.GET)
        if form.is_valid():
            chars.append(form.cleaned_data['first_char'])
            chars.append(form.cleaned_data['second_char'])
            chars.append(form.cleaned_data['third_char'])

            for char in chars:
                available_lines = Line.objects.filter(firstletter=char)
                random_line = available_lines[random.randrange(
                    len(available_lines))].content
                lines.append(random_line)

    else:
        form = GeneratePoemForm()

    context = {'form': form, 'poem': lines}
    return render(request, 'poem_gen/get_poem.html', context)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'glad you could join us!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}

    return render(request, 'poem_gen/register.html', context)

def return_user(request):
    if request.user.is_authenticated is not None:
        user = request.user.is_authenticated
    else:
        user = None

    return user

def view_notebook(request):
    everyline = Line.objects.all()
    if not everyline:
        context = {'message': 'lines yet to be written'}
    else:
        data = []
        for each in everyline:
            data.append({
                'id': each.id, 
                'content': each.content, 
                'author': each.author
                })
    
        context = {'data': data}
    return render(request, 'poem_gen/view_notebook.html', context)

def write_line(request):
    user = request.user

    if request.method == 'POST':
        form = WriteLineForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.firstletter = request.POST['content'][0]
            form.instance.author = CustomUser.objects.get(username=user)
            form.save()
            messages.success(request, "you've been published!")
            return redirect('index')
    else:
        form = WriteLineForm()
    
    context = {'form': form, 'user': user} 
    return render(request, 'poem_gen/write_line.html', context)
