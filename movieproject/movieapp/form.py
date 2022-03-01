from django import forms
from . models import Movie

class Movie_update(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','desc','mini_desc','Year','img']