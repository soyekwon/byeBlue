import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bye_blue.settings")
import django
django.setup()
from online_class.models import CrollData

def croll_data():
    crolldata = CrollData.objects.all()
    crolldata.delete()
    req = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=view&query=%ED%99%88%EB%B2%A0%EC%9D%B4%ED%82%B9&oquery=%EB%B2%A0%EC%9D%B4%ED%82%B9&tqi=hf4D8lprvh8ssEOqZOlssssssKo-385442&mode=normal')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select(".total_area > a")
    data = {}

    cnt = 0
    for title in my_titles:
        if(cnt == 5):
            break
        else:
            data[title.text] = title['href']
        cnt += 1
        
        
    return data

# 이 명령어는 이 파일이 import가 아닌 python에서 직접 실행할 경우에만 아래 코드가 동작하도록 합니다.
if __name__=='__main__':
    croll_data_dict = croll_data()
    for t, l in croll_data_dict.items():
        CrollData(title=t, link=l).save()

# def parse_youtube():
#     req = requests.get('https://www.youtube.com/results?search_query=%EB%B2%A0%EC%9D%B4%ED%82%B9')
#     html = req.text
#     soup = BeautifulSoup(html, 'html.parser')
#     my_titles = soup.select('#video-title')
    

#     cnt = 0
#     data = {}

#     for title in my_titles:

#         if(cnt == 5):
#             break

#         else:
#             data[title.text] = title.get('href')
#             cnt += 1

#     return data

# if __name__=='__main__':
#     blog_data_dict = parse_youtube()
#     for t, l in blog_data_dict.items():
#         CrollData(title=t, link=l).save()









