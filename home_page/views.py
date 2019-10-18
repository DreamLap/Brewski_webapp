from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import JournalForm, JournalEntryForm
from .models import create_journal as cj
from .models import register_user

  
# Create your views here.

def home_page(request):
    return render(request, 'home_page.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

def create_journal(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = JournalForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            cj(form.cleaned_data)
            # redirect to a new URL:
            form = JournalEntryForm()
            return render(request, 'journal_entry.html', {'form': form})
            #return HttpResponseRedirect('home_page.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = JournalForm()

    return render(request, 'Create_Journal.html', {'form': form})


	
	
	
	
	