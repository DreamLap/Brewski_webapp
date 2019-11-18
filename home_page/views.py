from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .DBManager import DBManager
from .forms import JournalFormSection0
from .forms import JournalFormSection1
from .forms import JournalFormSection2
from .forms import JournalFormSection3
from .models import create_journal as cj
from .models import edit_journal as ej
from .models import register_user
from .autofill_form import autofill_form

import boto3


  
# Create your views here.
@login_required
def profile_page(request):
    is_logged_in = True
    DB = DBManager.getInstance()
    data = DB.getAllJournals()

    #checks to see if user has create a favorties journal
    favorite_list = DB.getFavoriteJournalList(request.user)
    print('fav list: ', favorite_list)
    return render(request, 'profile.html', {'data': data,'is_logged_in' : is_logged_in, 'favorite_list' : favorite_list})

def home_page(request):
    print(request.user)
    is_logged_in = True
    DB = DBManager.getInstance()
    data = DB.getAllJournals()
    return render(request, 'home_page.html', {'data': data,'is_logged_in' : is_logged_in})

#def login(request):
    #print('login request')
#   return render(request, 'login.html')

def edit_journal(request, journal_id):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form0 = JournalFormSection0(request.POST)
        form1 = JournalFormSection1(request.POST)
        form2 = JournalFormSection2(request.POST)
        form3 = JournalFormSection3(request.POST)
        if form0.is_valid():
            print('FORM0 is valid!!!')
        if form0.is_valid() and form1.is_valid() and form2.is_valid() and form3.is_valid():
            # process the data in form.cleaned_data as required
            form0_clean = form0.cleaned_data
            form1_clean = form1.cleaned_data
            form2_clean = form2.cleaned_data
            form3_clean = form3.cleaned_data
            combine_form_clean = {}
            combine_form_clean.update(form0_clean)
            combine_form_clean.update(form1_clean)
            combine_form_clean.update(form2_clean)
            combine_form_clean.update(form3_clean)
            ej(combine_form_clean, str(request.user), journal_id)
            return profile_page(request)

        else:
            print('sorry fam')


    else:
        DB = DBManager.getInstance()
        data = DB.getAllJournals()
        for entry in data:
            #found a match in DB
            if journal_id == str(entry['id']):
                #auth that the user is able to edit
                if str(request.user) == str(entry['UserID']):
                    print('you can edit this journal: ' , entry['id'])

                    #auto populates form with DB info
                    filled_out_form = autofill_form(entry, 0)
                    form0 = JournalFormSection0(filled_out_form)

                    filled_out_form = autofill_form(entry, 1)
                    form1 = JournalFormSection1(filled_out_form)

                    filled_out_form = autofill_form(entry, 2)
                    form2 = JournalFormSection2(filled_out_form)

                    filled_out_form = autofill_form(entry, 3)
                    form3 = JournalFormSection3(filled_out_form)


                    return render(request, 'edit_journal.html', {'entry': entry, 'form0': form0, 'form1': form1, 'form2': form2, 'form3': form3})
                #Journal exist but user isn't doesn't match UserID
                else:
                    error_message = 'Error: You do not have permission to edit this journal.'
                    return render(request, 'error_page.html', {'error_message': error_message})

        #no journal exist to edit
        error_message = 'Error: Journal ID %s does not exist.' % journal_id
        return render(request, 'error_page.html', {'error_message': error_message})

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
            
            #creates favorites list for user
            DB = DBManager.getInstance()
            DB.createFavoritesForUser(request.user)
            return redirect('/')

    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

@login_required
def create_journal(request):
    print('create journal')

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print('we in post')
        # create a form instance and populate it with data from the request:
        form0 = JournalFormSection0(request.POST)
        form1 = JournalFormSection1(request.POST)
        form2 = JournalFormSection2(request.POST)
        form3 = JournalFormSection3(request.POST)
        # check whether it's valid:
        if form0.is_valid() and form1.is_valid() and form2.is_valid() and form3.is_valid():
            # process the data in form.cleaned_data as required
            print("passed")
            form0_clean = form0.cleaned_data
            form1_clean = form1.cleaned_data
            form2_clean = form2.cleaned_data
            form3_clean = form3.cleaned_data
            combine_form_clean = {}
            combine_form_clean.update(form0_clean)
            combine_form_clean.update(form1_clean)
            combine_form_clean.update(form2_clean)
            combine_form_clean.update(form3_clean)
            cj(combine_form_clean, str(request.user))
            # redirect to a new URL:

            return HttpResponseRedirect('/')


    # if a GET (or any other method) we'll create a blank form
    else:
        print(request.user)
        print('this shouldnt appear twice')
        form0 = JournalFormSection0()
        form1 = JournalFormSection1()
        form2 = JournalFormSection2()
        form3 = JournalFormSection3()


    return render(request, 'Create_Journal.html', {'form0': form0, 'form1': form1, 'form2': form2, 'form3': form3})

def journal_page(request,recipe_id):
    #is_logged_in = True
    DB = DBManager.getInstance()
    data = DB.getAllJournals()
    for entry in data:
        if recipe_id == str(entry['id']):
            print('entry page: ', entry['id'])
            isJournalFavorited = DB.checkUserFavoritedList(str(request.user), recipe_id)
            return render(request, 'journal_page.html',{'entry': entry, 'isJournalFavorited': isJournalFavorited})
        
    error_message = 'Error: Journal ID %s does not exist.' % recipe_id
    return render(request, 'error_page.html', {'error_message': error_message})

def delete_journal(request, journal_id):
    print('delete_journal call')
    DB = DBManager.getInstance()
    journal_entry = DB.getItemByID(journal_id, 'Journal')

    if journal_entry == None:
        error_message = 'Journal %s does not exist' % journal_id
        return render(request, 'error_page.html', {'error_message': error_message})

    elif str(request.user) != str(journal_entry['UserID']):
        error_message = 'You do not have permission to delete journal %s.' % journal_id
        return render(request, 'error_page.html', {'error_message': error_message})

    DB.deleteItemByID(journal_id, 'Journal')
    return redirect('/')

@login_required
def favorite_journal(request, journal_id):
    if request.user.is_authenticated:
        print('you are logged in')
    else:
        print('you are not logged in')
        return profile_page(request)
        
    DB = DBManager.getInstance()
    journal_entry = DB.getItemByID(journal_id, 'Journal')

    if journal_entry == None:
        error_message = 'Journal %s does not exist' % journal_id
        return render(request, 'error_page.html', {'error_message': error_message})
    
    DB.favoriteJournalByID(journal_id, request.user)
    DB.getFavoriteJournalList(request.user)
    return journal_page(request, journal_id)

def delete_favorite_journal(request, journal_id):
    DB = DBManager.getInstance()
    DB.removeJournalFromFavorites(journal_id, request.user)
    return journal_page(request, journal_id)
