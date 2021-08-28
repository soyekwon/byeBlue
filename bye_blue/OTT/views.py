from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator
from account.models import User
from django.http import HttpResponse

# Create your views here.


def delete(request, pk):
    ott_board = get_object_or_404(OTT, id=pk)
    ott_board.delete()
    return redirect("/OTT/list")


def edit(request, pk):
    if request.method == "GET":
        ott_board = get_object_or_404(OTT, id=pk)
        res = {}
        if ott_board is None:
            res["error"] = "게시물이 존재하지 않습니다"
            return render(request, "OTT/list.html", res)
        else:
            if request.session.get("name") == ott_board.writer:
                data = {}
                data["board"] = ott_board
                data["pk"] = pk
                return render(request, "OTT/edit.html", data)
            else:
                res["error"] = "글 수정 권한이 없습니다"
                return redirect("/OTT/list")
    else:
        genre = request.POST["genre"]
        title = request.POST["title"]
        contents = request.POST["contents"]
        board = OTT.objects.get(id=pk)

        if request.session.get("name") == board.writer:
            name = board.writer
            board.genre = genre
            board.title = title
            board.contents = contents
            board.name = name
            board.save()
            res = {}
            res["error"] = "글 수정 완료"
            return redirect("/OTT/view/" + str(pk))
        else:
            res = {}
            res["error"] = "글 수정 권한이 없습니다"
            return redirect("/OTT/list", res)


from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
import copy
import time
import threading


# def delete():
#     Netflix.delete()
#     threading.Timer(86400, delete).start()


# delete()


def list(request):

    list_mess = {}

    if not Netflix.objects.all():
        netflix_url = "https://www.4flix.co.kr/netflixranking/"

        driver = webdriver.Edge("msedgedriver.exe")
        driver.get(netflix_url)
        soup = bs(driver.page_source, "html.parser")
        driver.close()

        name = soup.select("span#n-title")
        # image = soup.select('img[class="style-scope yt-img-shadow"]')

        name_list = []

        for i in range(len(name)):
            name_list.append(name[i].get_text())

        netflixDic = {"title": name_list}

        netflixDf = pd.DataFrame(netflixDic)

        netflixDf.to_csv("넷플릭스 인기순위.csv", encoding="", index=False)

        for i in range(0, len(name_list)):
            netflix = Netflix
            netflix(title=name_list[i]).save()

    all_ott_netflix = Netflix.objects.all()
    list_mess["netflix_board"] = all_ott_netflix[:5]

    # session을 지워주면

    if request.session.get("email"):
        list_mess["name"] = request.session["name"]

    all_ott_board = OTT.objects.all().order_by("-write_date")
    list_mess["print_list"] = all_ott_board
    page = int(request.GET.get("p", 1))
    pagenator = Paginator(all_ott_board, 10)
    list_mess["ott_board"] = pagenator.get_page(page)

    return render(request, "OTT/list.html", list_mess)


def view(request, pk):
    context = {}
    board = get_object_or_404(OTT, id=pk)
    context["board"] = board
    context["session_name"] = request.session["name"]

    comment_board = OTT_COMMENT.objects.filter(board=pk)
    context["comment"] = comment_board

    return render(request, "OTT/view.html", context)


def write(request):
    if request.method == "POST":
        genre = request.POST["genre"]
        title = request.POST["title"]
        contents = request.POST["contents"]
        funny = request.POST["funny"]
        name = request.session.get("name")
        # user = User.objects.get(pk = name)# ->writer=user로 넘길때 사용
        # print(user)
        ott_board = OTT
        if "2" == str(funny):
            funny = str("재밌어요~!")
        elif "1" == str(funny):
            funny = str("보통이에요!")
        else:
            funny = str("너무 재밌어요^-^")

        ott_board(
            genre=genre, title=title, contents=contents, writer=name, funny=funny
        ).save()

        return redirect("/OTT/list")
    else:
        return render(request, "OTT/write.html")


def comment(request, pk):
    if request.method == "POST":
        contents = request.POST["contents"]
        board = get_object_or_404(OTT, id=pk)
        writer = request.session["name"]

        ott_comment = OTT_COMMENT()

        ott_comment.board = board
        ott_comment.contents = contents
        ott_comment.writer = writer
        ott_comment.save()

        return redirect("/OTT/view/" + str(pk))
    else:
        res = {}
        res["PK"] = pk
        return render(request, "OTT/comment.html", res)
