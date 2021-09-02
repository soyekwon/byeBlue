from . import views
from django.urls import path

app_name = 'mbti'

urlpatterns = [
    path('', views.index, name='index'),
    

]

