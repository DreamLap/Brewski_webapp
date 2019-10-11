from django.conf.urls import url
from . import views
from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views

app_name = 'home_page'

urlpatterns = [
    url('create_journal/', views.create_journal, name = 'create_journal'),
	url('create_journal/', views.create_journal, name = 'create_journal'),
    url('login/', LoginView.as_view(template_name='login.html'), name = 'login'),
    url('register/', views.register, name = 'register'),
    url('', views.home_page),
]