from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect

from .forms import JournalForm
import boto3
  
# Create your views here.

def index(request):
    return render(request, 'home_page/home_page.html')


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = JournalForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            dynamodb = boto3.resource('dynamodb', 
                               region_name='us-east-1',
                               aws_access_key_id='AKIAJTNALKALUKKL3XUQ',
                               aws_secret_access_key='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')
			table = dynamodb.Table('Journal')
			table.put_item(
			Item={
					'JournalID': form.cleaned_data,
				}
			)
			
            # redirect to a new URL:
            return HttpResponseRedirect('/home_page/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = JournalForm()

    return render(request, 'Create_Journal.html', {'form': form})