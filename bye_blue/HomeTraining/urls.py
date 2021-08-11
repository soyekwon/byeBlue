from django.urls import path
import HomeTraining.views
import main.views

app_name = 'HomeTraining'

urlpatterns = [
    path('edit/<int:pk>',HomeTraining.views.edit,name="edit"),
    path('list/',HomeTraining.views.list,name="list"),
    path('view/<int:pk>',HomeTraining.views.view,name="view"),
    path('write/',HomeTraining.views.write,name="write"),
    path('delete/<int:pk>',HomeTraining.views.delete,name="delete"),

]