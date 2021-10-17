from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,name="index"),
    path("<int:soru_id>",views.soru,name="soru"),
    path("<int:soru_postid>/book",views.book,name="book"),

    ]