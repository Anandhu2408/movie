from django import forms
from details.models import Movie


class movieform(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'