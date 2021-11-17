from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'overview', 'poster_path',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user' ,'content', 'rank')
