from django import forms
from .models import MovieList, ActorList

class MovieListForm(forms.ModelForm):
    class Meta:
        model = MovieList
        fields = ["title", "year", "plot", "actor"]

class ActorListForm(forms.ModelForm):
    class Meta:
        model = ActorList
        fields = ["name", "gender", "birthdate", "bio"]
