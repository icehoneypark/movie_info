from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_safe
from .models import Movie, Comment
from .forms import MovieForm, CommentForm


def movie_index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment_form = CommentForm()
    comments = movie.comment_set.all()
    context = {
        'movie': movie,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'community/detail.html', context)