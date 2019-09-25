from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    #path('', views.index, name= 'index'),
    url(r'^$', views.index),
    url(r'^login/$', login, {'template_name': 'home_page/login.html'})
]