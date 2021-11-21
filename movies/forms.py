from django import forms
from .models import Movie, MovieReview

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ('content', 'rank',)