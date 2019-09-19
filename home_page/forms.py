from django import forms

class JournalForm(forms.Form):
    your_name = forms.CharField(label='JournalName', max_length=100)