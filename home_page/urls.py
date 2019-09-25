from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    url(r'^$', views.home_page),
	path(''views.get_name, name = 'get_name'),
]