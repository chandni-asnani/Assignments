from django.contrib import admin
from django.urls import path, include
from .views import LoginView, SignUpView
from registration.views import LogoutView
from issue.views import BookView


urlpatterns = [
path("signup", SignUpView.as_view() , name = 'signup'),
path("logout", LogoutView.as_view() , name = 'logout')
]