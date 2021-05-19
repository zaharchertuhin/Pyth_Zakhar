from django import forms
from revies.models import Review
class Revies_form(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["name", "email", "revies", "rating"]
    # name = forms.CharField(max_length=25)
    # email = forms.EmailField()
    # review = forms.CharField(widget=forms.Textarea)