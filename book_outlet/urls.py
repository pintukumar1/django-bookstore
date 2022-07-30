from django import views
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:id>",  views.book_detail, name="book_detail")
]


