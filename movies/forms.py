from django import forms
from .models import Movie, MovieComment

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieCommentForm(forms.ModelForm):
    class Meta:
        model = MovieComment
        fields = ('content', 'rank')