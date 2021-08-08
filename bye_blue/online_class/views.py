from django.shortcuts import redirect, render, get_object_or_404
from .models import Online
from django.utils import timezone
from django.db import models
from account.models import User
from .forms import OnlineForm


def index(request):
    online_object = Online.objects.all()
    return render(request, 'class/class.html', {'online_objects' : online_object})

def detail(request, id):
    online_object = get_object_or_404(Online, pk = id)
    return render(request, "class/class_detail.html", {'online_object' : online_object})

def write(request):
    return render(request, "class/class_write.html")

def create(request):

    if request.method == 'POST':
        form = OnlineForm(request.POST)
        if form.is_valid():
            online = form.save(commit=False)
            online.writer = request.user
            online.pub_date = timezone.now()
            online.save()
            return redirect('online_class:index')
        
    else:
        form = OnlineForm()
    
    context = {'form':form}

    return render(request, 'class/class_write.html', context)

def edit(request, id):
    edit_object = get_object_or_404(Online, pk = id)
    edit_object.title = request.POST.get('title', '')
    edit_object.content = request.POST.get('content', '')
    edit_object.pub_date = timezone.datetime.now()
    edit_object.save()

    return redirect(str(edit_object.id)+'/edit')









