from django import views
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index)
]


