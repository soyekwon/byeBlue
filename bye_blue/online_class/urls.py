from . import views
from django.urls import path

app_name = 'online_class'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('write/', views.create, name='write'),
    path('<int:id>/edit/', views.edit, name='edit'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:online_id>/commment_edit/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('<int:online_id>/commment_delete/<int:comment_id>', views.comment_delete,name='comment_delete'),

]

