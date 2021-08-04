from django.shortcuts import render
from .models import Online

def index(request):
    online_object = Online.objects.all()
    return render(request, 'class/class.html', {'online_objects' : online_object})






