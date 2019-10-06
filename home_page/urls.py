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
<<<<<<< HEAD
    #path('', views.index, name= 'index'),
    url(r'^$', views.index),
    url(r'^login/$', login, {'template_name': 'home_page/login.html'})
=======
	  path(''views.get_name, name = 'create_journal'),
    url('login/', views.login, name = 'login'),
    url('get_name/', views.get_name, name = 'get_name'),
    url('register/', views.register, name = 'register'),
    url('', views.home_page),
>>>>>>> 64011ffbbf0288e0cafdde3c0d28eafb71021200
]