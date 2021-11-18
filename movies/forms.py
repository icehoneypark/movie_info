from django import forms
from .models import Movie, MovieComment

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'overview', 'poster_path',)


class MovieCommentForm(forms.ModelForm):
    class Meta:
        model = MovieComment
        fields = ('user' ,'content', 'rank')
