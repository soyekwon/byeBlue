from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import User

def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        pw = request.POST['PW']
        pw2 = request.POST['PW2']

        res_data ={}

        if name =="" or email =="" or pw =="" or pw2 =="":
            res_data['error'] = "입력되지 않은 값이 있습니다"
            return render(request,"signup.html",res_data)
        if pw != pw2:
            res_data['error'] = "비밀번호가 일치하지 않습니다"
            return render(request,"signup.html",res_data)

        #중복가입 방지 -> 다시 생각해봐야함
        member = User
        print(type(member))

        if member.objects.filter(email=email).exists():
            res_data['error'] = "이미 가입된 이메일[ID]입니다"
            return render(request,"signup.html",res_data)
        else:
            member(name = name, email = email, pw = pw).save()
            return redirect('/')
  

    else:
        return render(request,"signup.html")



def login(request):
    if request.method == "POST":
        email=request.POST["email"]
        pw =request.POST["pw"]

        members= User
        data = members.objects.get(email = email)
        print(data)
        res_data ={}

        if data is None:
            res_data['error']="회원정보를 찾을 수 없습니다"
            return render(request,'login.html',res_data)
        else:
            if data.pw == pw:
                request.session['email'] = email
                request.session['name'] = data.name
                request.session.permanent = True #자원의 효율적 운영을 위해 true로 놓음
                return redirect('/')
            else:
                res_data['error'] = "비밀번호가 일치하지 않습니다"
                return render(request,"login.html",res_data)
    else:
        return render(request,"login.html")


def logout(request):
    #session을 지워주면 됨
    try:#로그아웃했을때 로그인 안 되도록
        if request.session.get('User'):
            del(request.session['user'])
    except:
        pass
    return redirect('/')
