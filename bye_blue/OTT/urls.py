from django.urls import path
import OTT.views
import main.views

app_name = "OTT"

urlpatterns = [
    path("edit/<int:pk>", OTT.views.edit, name="edit"),
    path("list/", OTT.views.list, name="list"),
    path("view/<int:pk>", OTT.views.view, name="view"),
    path("write/", OTT.views.write, name="write"),
    path("delete/<int:pk>", OTT.views.delete, name="delete"),
    path("comment/<int:pk>", OTT.views.comment, name="comment"),
]
