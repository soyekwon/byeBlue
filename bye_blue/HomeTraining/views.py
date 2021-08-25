from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator
from account.models import User
from django.http import HttpResponse


def delete(request, pk):
    ht_board = get_object_or_404(HT, id=pk)
    ht_board.delete()
    return redirect("/HomeTraining/list")


def edit(request, pk):
    if request.method == "GET":
        ht_board = get_object_or_404(HT, id=pk)
        res = {}
        if ht_board is None:
            res["error"] = "게시물이 존재하지 않습니다"
            return render(request, "HomeTraining/list.html", res)
        else:
            if request.session.get("name") == ht_board.writer:
                data = {}
                data["board"] = ht_board
                data["pk"] = pk
                return render(request, "HomeTraining/edit.html", data)
            else:
                res["error"] = "글 수정 권한이 없습니다"
                return redirect("/HomeTraining/list")
    else:
        part = request.POST["part"]
        title = request.POST["title"]
        contents = request.POST["contents"]
        board = HT.objects.get(id=pk)

        if request.session.get("name") == board.writer:
            name = board.writer
            board.part = part
            board.title = title
            board.contents = contents
            board.name = name
            board.save()
            res = {}
            res["error"] = "글 수정 완료"
            return redirect("/HomeTraining/view/" + str(pk))
        else:
            res = {}
            res["error"] = "글 수정 권한이 없습니다"
            return redirect("/HomeTraining/list", res)


from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
import copy


def youtube(request):
    keyword = "홈트레이닝"
    target_url = "https://www.youtube.com/results?search_query={}".format(keyword)

    driver = webdriver.Edge("C:\\bye_blue_sujin\\byeBlue\\bye_blue\\msedgedriver.exe")
    driver.get(target_url)
    soup = bs(driver.page_source, "html.parser")
    driver.close()

    name = soup.select("a#video-title")
    video_url = soup.select("a#video-title")
    view = soup.select("a#video-title")
    # image = soup.select('img[class="style-scope yt-img-shadow"]')

    name_list = []
    url_list = []
    view_list = []

    for i in range(len(name)):
        name_list.append(name[i].get("title"))
        view_list.append(view[i].get("aria-label").split()[-1])
    for i in video_url:
        url_list.append("{}{}".format("https://www.youtube.com", i.get("href")))

    youtubeDic = {"title": name_list, "url": url_list, "click": view_list}

    youtubeDf = pd.DataFrame(youtubeDic)

    youtubeDf.to_csv("홈트레이닝유튜브.csv", encoding="", index=False)

    for i in range(0, len(name_list)):
        youtube = YoutubeHt
        youtube(
            youtube_title=name_list[i],
            youtube_url=url_list[i],
            youtube_view=view_list[i],
        ).save()


def list(request):

    list_mess = {}
    all_ht_youtube = YoutubeHt.objects.all().order_by("-youtube_view")
    if not all_ht_youtube:
        youtube()
    list_mess["youtube_board"] = all_ht_youtube[:5]

    if request.session.get("email"):
        list_mess["name"] = request.session["name"]

    all_ht_board = HT.objects.all().order_by("-write_date")
    list_mess["print_list"] = all_ht_board
    page = int(request.GET.get("p", 1))
    pagenator = Paginator(all_ht_board, 3)
    list_mess["ht_board"] = pagenator.get_page(page)

    return render(request, "HomeTraining/list.html", list_mess)


def view(request, pk):
    context = {}
    board = get_object_or_404(HT, id=pk)
    context["board"] = board
    context["session_name"] = request.session["name"]

    comment_board = HT_COMMENT.objects.filter(board=pk).order_by("-write_date")
    context["comment"] = comment_board

    return render(request, "HomeTraining/view.html", context)


def write(request):
    if request.method == "POST":
        part = request.POST["part"]
        title = request.POST["title"]
        contents = request.POST["contents"]
        name = request.session.get("name")
        images = request.FILES.get("images")

        ht_board = HT
        ht_board(
            part=part, title=title, contents=contents, writer=name, images=images
        ).save()

        return redirect("/HomeTraining/list")
    else:
        return render(request, "HomeTraining/write.html")


def comment(request, pk):
    if request.method == "POST":
        contents = request.POST["contents"]
        board = get_object_or_404(HT, id=pk)
        writer = request.session["name"]

        ht_comment = HT_COMMENT()

        ht_comment.board = board
        ht_comment.contents = contents
        ht_comment.writer = writer
        ht_comment.save()

        return redirect("/HomeTraining/view/" + str(pk))
    else:
        res = {}
        res["PK"] = pk
        return render(request, "HomeTraining/comment.html", res)
