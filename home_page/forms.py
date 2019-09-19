from django import forms

class JournalForm(forms.Form):
    journal_name = forms.CharField(label='JournalName', max_length=100)