from django.shortcuts import render
from .models import Mbti

def index(request):
    content = {}
    if request.session.get("name"):
        content['name'] = request.session["name"]


    return render(request, "mbti/mbti_list.html", content)


# Create your views here.
