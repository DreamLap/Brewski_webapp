from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .DBManager import DBManager
from .forms import JournalFormSection1
from .forms import JournalFormSection2
from .models import create_journal as cj
from .models import register_user
import boto3
  
# Create your views here.

def index(request):
    return render(request, 'home_page/home_page.html')


def home_page(request):
    return render(request, 'home_page.html')
    #DB = DBManager.getInstance()
    #data = DB.getAllJournals()
    #print(data)
    #return render(request, 'home_page.html', {"data": data})

#def login(request):
#    print('login request')
#   return render(request, 'login.html')


def logout_view(request):
    print('logout hit')
    logout(request)
    return HttpResponseRedirect('/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')

    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

def create_journal(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form1 = JournalFormSection1(request.POST)
        form2 = JournalFormSection2(request.POST)
        # check whether it's valid:
        if form1.is_valid() and form2.is_valid():
            # process the data in form.cleaned_data as required
            form1_clean = form1.cleaned_data
            form2_clean = form2.cleaned_data
            combine_form_clean = {}
            combine_form_clean.update(form1_clean)
            combine_form_clean.update(form2_clean)
            cj(combine_form_clean)
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form1 = JournalFormSection1()
        form2 = JournalFormSection2()

    return render(request, 'Create_Journal.html', {'form1': form1, 'form2': form2})
