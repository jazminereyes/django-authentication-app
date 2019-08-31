# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect 
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
        else: 
            error = "Your username must be 150 characters or fewer. Letters, digits and @/./+/-/_ only. Make sure that the password is not too similar to the username and must contain at least 8 characters."
            return render(request, 'registration/register.html', {'form': form, 'error': error})
    else: 
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})