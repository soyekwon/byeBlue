from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib import messages
from .models import Online, Comment, CrollData
from account.models import User
from .forms import OnlineForm, CommentForm
import requests
from bs4 import BeautifulSoup


def index(request):
    list_object = {}
    crolldata = CrollData.objects.all()
    list_object['crollData'] = crolldata
    if request.session.get('email'):
        list_object['name'] = request.session['name']

    online_object = Online.objects.all().order_by('-id')
    list_object['objects'] = online_object
    page = int(request.GET.get('p', 1))
    pagenator = Paginator(online_object, 5)
    list_object['page'] = pagenator.get_page(page)

    return render(request, 'class/class.html', list_object)


def detail(request, id):
    online_object = get_object_or_404(Online, pk = id)
    comments = Comment.objects.filter(board=id)

    context={}
    context['online_object']=online_object
    context['session_name'] = request.session['name']

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comments = comment_form.save(commit=False)
            text = comment_form.cleaned_data['text']
            comments.board = online_object
            comments.pub_date = timezone.now()
            comments.free_id = id
            comments.writer = request.session['name']
            comments.save()
            print(text)
            return redirect('/online_class/' + str(online_object.id))
        
    else:
        comment_form = CommentForm()

    context['comments'] = comments
    context['comment_form'] = comment_form


    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        

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

def comment_edit(request, online_id, comment_id):
    board = get_object_or_404(Online, id=online_id)
    comments = Comment.objects.filter(board=online_id)
    my_comment = Comment.objects.get(id=comment_id)
    comment_form = CommentForm(instance=my_comment)

    if request.method == "POST":
        update_comment_form = CommentForm(request.POST, instance=my_comment)
        if update_comment_form.is_valid():
            update_comment_form.save()

            return redirect('/online_class/'+str(board.id))

    context={
        'board':board,
        'comments':comments,
        'comment_form':comment_form,
        'my_comment':my_comment,
    }

    return render(request, 'class/class_comment_edit.html', context)

def comment_delete(request, online_id, comment_id):
    board = Online.objects.get(id=online_id)
    comment = Comment.objects.get(id=comment_id)

    if request.session.get('name') != comment.writer :
        messages.warning(request, '권한없음')
        return redirect('/online_class/'+str(board.id))
    
    if request.method == "POST":
        comment.delete()
        return redirect('/online_class/'+str(board.id))
    
    
    context={
        'comment':comment,
        'board':board
    }
    return render(request, 'class/class_comment_delete.html',context)

def croll(requests):

    req = requests.get('https://www.youtube.com/results?search_query=베이킹')

    html = req.text

    soup = BeautifulSoup(html, 'html.parser')

    my_titles = soup.select('#video-title')

    cnt = 0

    for title in my_titles:

        if(cnt == 5):
            break

        else:
            print(title.text)
            print(title.get('href'))
            cnt += 1
    
    









