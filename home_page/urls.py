from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth.views import LoginView

app_name = 'home_page'

urlpatterns = [

    url('profile/', views.profile_page, name = 'profile'),
    url('logout/', views.logout_view, name = 'logout_view'),
    path('delete_journal/<str:journal_id>', views.delete_journal, name = 'delete_journal'),
    path('favorite_journal/<str:journal_id>', views.favorite_journal, name = 'favorite_journal'),
    path('delete_favorite_journal/<str:journal_id>', views.delete_favorite_journal, name = 'delete_favorite_journal'),
	url('create_journal/', views.create_journal, name = 'create_journal'),
    url('login/', LoginView.as_view(template_name='login.html'), name = 'login'),
    path('edit_journal/<str:journal_id>', views.edit_journal, name = 'edit_journal'),
    url('register/', views.register, name = 'register'),
    path('journal_page/<str:recipe_id>', views.journal_page, name = 'journal_page'), 
    url('', views.home_page)
]