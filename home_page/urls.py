from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth.views import LoginView

app_name = 'home_page'

urlpatterns = [

    url('profile/', views.profile_page, name = 'profile'),
    url('logout/', views.logout_view, name = 'logout_view'),
	url('create_journal/', views.create_journal, name = 'create_journal'),
    url('login/', LoginView.as_view(template_name='login.html'), name = 'login'),
    path('edit_journal/<str:journal_id>', views.edit_journal, name = 'edit_journal'),
    url('register/', views.register, name = 'register'),
    url('', views.home_page),
]