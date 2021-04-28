from django import forms
class Revies_form(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    review = forms.CharField(widget=forms.Textarea)
