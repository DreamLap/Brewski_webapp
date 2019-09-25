from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'home_page'

urlpatterns = [
    url('get_name/', views.get_name, name = 'get_name'),
    url('home_page/', views.get_name, name = 'home_page'),
    url('', views.home_page),
]