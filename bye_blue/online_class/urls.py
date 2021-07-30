from . import views
from django.urls import path

app_name = 'online_class'

urlpatterns = [
    path('', views.index, name='index'),
]