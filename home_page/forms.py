from django import forms

class JournalForm(forms.Form):
	journal_name = forms.CharField(label='JournalName', max_length=100)


	
class JournalEntryForm(forms.Form):
	hop_name = forms.CharField(max_length=100)
	hop_alpha = forms.FloatField(min_value = 0.0, max_value = 100.0)
	hop_amount = forms.FloatField()
