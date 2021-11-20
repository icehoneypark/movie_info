from django.core import paginator
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_safe
from .models import Movie
from .forms import MovieCommentForm
from django.core.paginator import Paginator

def movie_index(request):
    movies = Movie.objects.all()
    top_10 = Movie.objects.order_by('-popularity')[:10]
    # paginator = Paginator(movies, 20)
    # page = request.GET.get('page')
    context = {
        'movies': movies,
        'top_10': top_10,
        # 'paginator': paginator,
        # 'page': page,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie_comment_form = MovieCommentForm()
    movie_comments = movie.moviecomment_set.all()
    context = {
        'movie': movie,
        'movie_comment_form': movie_comment_form,
        'movie_comments': movie_comments,
    }
    return render(request, 'movies/detail.html', context)