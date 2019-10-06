from django.conf.urls import url
from . import views
from django.urls import path
<<<<<<< HEAD
from django.conf.urls import url
from django.contrib.auth.views import login
=======
from django.contrib.auth.views import LoginView
>>>>>>> 64011ffbbf0288e0cafdde3c0d28eafb71021200
from . import views

app_name = 'home_page'

urlpatterns = [
	url('create_journal/', views.create_journal, name = 'create_journal'),
    url('login/', views.login, name = 'login'),
    url('register/', views.register, name = 'register'),
    url('', views.home_page),
>>>>>>> 64011ffbbf0288e0cafdde3c0d28eafb71021200
]