from django import forms
class Revies_form(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    review = forms.CharField(widget=forms.Textarea)

class Show_form(forms.Form):
    # sh_review = forms.CharField(widget=forms.Textarea)
    rating = forms.IntegerField(max_value=100, min_value=5)