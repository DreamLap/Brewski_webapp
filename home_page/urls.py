from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth.views import LoginView

app_name = 'home_page'

urlpatterns = [
	
    url(r'^login/$', LoginView.as_view(template_name='login.html'), name="login" ),
    url('create_journal/', views.create_journal, name = 'create_journal'),
    url('register/', views.register, name = 'register'),
    url('', views.home_page),
]