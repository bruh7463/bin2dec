from django import forms

class BinForm(forms.Form):
	bin_num = forms.CharField(label="Enter a binary number", max_length=100)