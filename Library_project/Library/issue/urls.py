from django.contrib import admin
from django.urls import path, include
from .views import BookView, Dashboard

urlpatterns = [
path("",  Dashboard.as_view(), name='dashboard'),
path("list",  BookView.as_view(), name='issuebook'),
]