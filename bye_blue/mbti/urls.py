from django.urls.resolvers import URLPattern
from . import views
from django.urls import path

app_name = 'mbti'

urlpatterns = [
    path('', views.list, name='list'),
]