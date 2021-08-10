from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator
from account.models import User
from django.http import HttpResponse

# Create your views here.

def delete(request,pk):
    ht_board = get_object_or_404(HT,id = pk)
    ht_board.delete()
    return redirect('/HomeTraining/list')

def edit(request,pk):
    if request.method == "GET":
        ht_board = get_object_or_404(HT,id = pk)
        res={}
        if ht_board is None:
            res['error']="게시물이 존재하지 않습니다"
            return render(request,'HomeTraining/list.html',res)
        else:
            if request.session.get("name") == ht_board.writer:
                data={}
                data["board"]=ht_board
                data["pk"] = pk
                return render(request,'HomeTraining/edit.html',data)
            else:
                res['error']="글 수정 권한이 없습니다"
                return redirect("/HomeTraining/list")
    else:
        part = request.POST['part']
        title = request.POST['title']
        contents = request.POST['contents']
        board = HT.objects.get(id = pk)

        if request.session.get("name") == board.writer:
            name = board.writer
            board.part = part
            board.title=title
            board.contents = contents
            board.name=name
            board.save()
            res={}
            res['error']="글 수정 완료"
            return redirect('/HomeTraining/view/'+str(pk)) 
        else:
            res={}
            res['error']="글 수정 권한이 없습니다"
            return redirect('/HomeTraining/list',res)    

def list(request):
        #session을 지워주면 
    list_mess ={}
    if request.session.get('email'):
            list_mess['name']=request.session['name']

    all_ht_board = HT.objects.all().order_by('-write_date')
    list_mess['print_list']=all_ht_board
    page = int(request.GET.get('p',1))
    pagenator = Paginator(all_ht_board,10)
    list_mess['ht_board']=pagenator.get_page(page)

    return render(request,"HomeTraining/list.html",list_mess)



def view(request,pk):
    context={}
    board = get_object_or_404(HT,id = pk)
    context['board']=board
    context['session_name']=request.session['name']

    comment_board = HT_COMMENT.objects.all().order_by('-write_date')
    context['comment']=comment_board
   
    return render(request,"HomeTraining/view.html",context)




def write(request):
    if request.method == "POST":
        part = request.POST['part']
        title = request.POST['title']
        contents = request.POST['contents']
        name = request.session.get('name')
        #user = User.objects.get(pk = name)# ->writer=user로 넘길때 사용
        #print(user)
        ht_board = HT
        ht_board(part = part, title = title, contents = contents,writer = name).save()
    

        return redirect('/HomeTraining/list')
    else:
        return render(request,'HomeTraining/write.html')

def comment(request,pk):
    if request.method == "POST":
        contents = request.POST['contents']
        board = get_object_or_404(HT,id=pk)
        writer = request.session['name']

        ht_comment = HT_COMMENT()
        
        ht_comment.board = board
        ht_comment.contents =contents
        ht_comment.writer = writer
        ht_comment.save()

        return redirect('/HomeTraining/view/'+str(pk))
    else:
        res={}
        res['PK']=pk
        return render(request,'HomeTraining/comment.html',res)

        
        

        

        

        
