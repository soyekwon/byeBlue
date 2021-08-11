from django.shortcuts import redirect, render, get_object_or_404
from .models import Online
from django.utils import timezone
from django.db import models
from account.models import User
from .forms import OnlineForm
from django.contrib import messages


def index(request):
    list_object = {}
    if request.session.get('email'):
        list_object['name'] = request.session['name']

    online_object = Online.objects.all().order_by('-id')
    list_object['objects'] = online_object
    return render(request, 'class/class.html', list_object)

def detail(request, id):
    context={}
    online_object = get_object_or_404(Online, pk = id)
    context['online_object']=online_object
    context['session_name'] = request.session['name']
    return render(request, "class/class_detail.html", context)

def write(request):
    return render(request, "class/class_write.html")

def create(request):

    if request.method == 'POST':
        form = OnlineForm(request.POST)
        if form.is_valid():
            online = form.save(commit=False)
            online.writer = request.session.get('name')
            online.pub_date = timezone.now()
            online.save()
            return redirect('online_class:index')
        
    else:
        form = OnlineForm()
    
    context = {'form':form}

    return render(request, 'class/class_write.html', context)

def edit(request, id):
    edit_object = get_object_or_404(Online, pk = id)

    if request.method == 'POST':
        form = OnlineForm(request.POST, instance=edit_object)
        if form.is_valid():
            edit_object = form.save(commit=False)
            edit_object.writer = request.session.get('name')
            edit_object.pub_date = timezone.now()
            edit_object.save()
            return redirect('online_class:index')
        
    else:
        form = OnlineForm(instance=edit_object)
    
    context = {'form':form}
    return render(request, 'class/class_write.html', context)

def delete(request, id):
    delete_object = get_object_or_404(Online, pk = id)
    delete_object.delete()
    return redirect('online_class:index')

    
    









