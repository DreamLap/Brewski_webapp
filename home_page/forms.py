from django import forms
from django.utils.safestring import mark_safe
from datetime import date

class JournalFormSection0(forms.Form):

	Name_of_brew = forms.CharField(max_length=100)
	Overall_notes = forms.CharField(widget = forms.Textarea, required = False)
	Completed = forms.BooleanField(required=False)
	Date = forms.DateField(initial=date.today(),widget=forms.HiddenInput())

class JournalFormSection1(forms.Form):
	
	Water_Volume = forms.FloatField(min_value = 0)
	Step_Mash_1_temp = forms.FloatField(min_value = 0.0)
	Step_Mash_1_time = forms.FloatField(min_value = 0.0)
	Step_Mash_2_temp = forms.FloatField(min_value = 0.0, required = False)
	Step_Mash_2_time = forms.FloatField(min_value = 0.0, required = False)
	Step_Mash_3_temp = forms.FloatField(min_value = 0.0, required = False)
	Step_Mash_3_time = forms.FloatField(min_value = 0.0, required = False)
	Step_Mash_4_temp = forms.FloatField(min_value = 0.0, required = False)
	Step_Mash_4_time = forms.FloatField(min_value = 0.0, required = False)
	Step_Mash_5_temp = forms.FloatField(min_value = 0.0, required = False)
	Step_Mash_5_time = forms.FloatField(min_value = 0.0, required = False)
	Mash_out = forms.BooleanField(required = False)
	#Sparge = forms.BooleanField(required = False)
	Sparge_temp = forms.FloatField(min_value = 0, required = False)
	Sparge_time = forms.FloatField(min_value = 0, required = False)
	Recirc_time = forms.FloatField(min_value = 0.0, required = False)
	Mash_notes = forms.CharField(widget = forms.Textarea, required = False)


class JournalFormSection2(forms.Form):
	Start_vol = forms.FloatField(min_value = 0.0, required = False)
	End_vol = forms.FloatField(min_value = 0.0, required = False)
	hop_name_1 = forms.CharField(max_length= 100.0, required = False)
	hop_amount_1 = forms.FloatField(min_value = 0.0, max_value = 200.0, required = False)
	hop_alpha_acid_1 = forms.FloatField(min_value = 0.0, required = False)
	hop_time_1 = forms.FloatField(min_value = 0.0, required = False)
	hop_name_2 = forms.CharField(max_length= 100.0, required = False)
	hop_amount_2 = forms.FloatField(min_value = 0.0, max_value = 200.0, required = False)
	hop_alpha_acid_2 = forms.FloatField(min_value = 0.0, required = False)
	hop_time_2 = forms.FloatField(min_value = 0.0, required = False)
	hop_name_3 = forms.CharField(max_length= 100.0, required = False)
	hop_amount_3 = forms.FloatField(min_value = 0.0, max_value = 200.0, required = False)
	hop_alpha_acid_3 = forms.FloatField(min_value = 0.0, required = False)
	hop_time_3 = forms.FloatField(min_value = 0.0, required = False)
	Whirlfloc = forms.BooleanField(required = False)
	Whirlpool_time = forms.FloatField(min_value=0.0, required = False)
	Boil_notes = forms.CharField(widget = forms.Textarea, required = False)

class JournalFormSection3(forms.Form):
	Yeast_name = forms.CharField(max_length = 100, required = False)
	Yeast_amount = forms.FloatField(min_value = 0.0, required = False)
	Start_gravity = forms.FloatField(min_value = 0.0, required = False) 
	temp_1 = forms.FloatField(min_value = 0.0, required = False)
	time_1 = forms.FloatField(min_value = 0.0, required = False)
	End_gravity_1 = forms.FloatField(min_value = 0.0, required = False)
	temp_2 = forms.FloatField(min_value = 0.0, required = False)
	time_2 = forms.FloatField(min_value = 0.0, required = False)
	End_gravity_2 = forms.FloatField(min_value = 0.0, required = False)
	temp_3 = forms.FloatField(min_value = 0.0, required = False)
	time_3 = forms.FloatField(min_value = 0.0, required = False)
	End_gravity_3 = forms.FloatField(min_value = 0.0, required = False)
	ABV = forms.FloatField(min_value = 0.0, required = False)
	Lager_temp = forms.FloatField(min_value = 0.0, required = False)
	Lager_time = forms.FloatField(min_value = 0.0, required = False)
	Fermentation_notes = forms.CharField(widget = forms.Textarea, required = False)
