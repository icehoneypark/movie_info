from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST
from django.contrib.auth.decorators import login_required
from .models import Movie, MovieReview
from .forms import MovieReviewForm


def movie_index(request):
    # movies = Movie.objects.all()
    # top_10 = Movie.objects.order_by('-popularity')[:10]
    # paginator = Paginator(movies, 20)
    # page = request.GET.get('page')
    top_1 = Movie.objects.order_by('-popularity')[0]
    top_2 = Movie.objects.order_by('-popularity')[1]
    top_3 = Movie.objects.order_by('-popularity')[2]
    top_4 = Movie.objects.order_by('-popularity')[3]
    top_5 = Movie.objects.order_by('-popularity')[4]
    top_6 = Movie.objects.order_by('-popularity')[5]
    top_7 = Movie.objects.order_by('-popularity')[6]
    top_8 = Movie.objects.order_by('-popularity')[7]
    top_9 = Movie.objects.order_by('-popularity')[8]
    top_10 = Movie.objects.order_by('-popularity')[9]
    context = {
        # 'movies': movies,
        # 'top_10': top_10,
        # 'paginator': paginator,
        # 'page': page,
        'top1': top_1,
        'top2': top_2,
        'top3': top_3,
        'top4': top_4,
        'top5': top_5,
        'top6': top_6,
        'top7': top_7,
        'top8': top_8,
        'top9': top_9,
        'top10': top_10,
    }
    return render(request, 'movies/index.html', context)

@require_safe
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review_form = MovieReviewForm()
    reviews = movie.moviereview_set.order_by('-pk')
    date_str1 = movie.released_date[0]
    date_str2 = movie.released_date[1]
    date_str3 = movie.released_date[2]
    date_str4 = movie.released_date[3]
    date_str5 = movie.released_date[5]
    date_str6 = movie.released_date[6]
    date_str7 = movie.released_date[8]
    date_str8 = movie.released_date[9]
    context = {
        'movie': movie,
        'review_form': review_form,
        'reviews': reviews,
        'date_str1': date_str1,
        'date_str2': date_str2,
        'date_str3': date_str3,
        'date_str4': date_str4,
        'date_str5': date_str5,
        'date_str6': date_str6,
        'date_str7': date_str7,
        'date_str8': date_str8,
    }
    return render(request, 'movies/detail.html', context)


@require_POST
def movie_review_create(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        review_form = MovieReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
        return redirect('movies:movie_detail', movie.pk)
    return redirect('movies:movie_index')


@login_required
def movie_review_update(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(MovieReview, pk=review_pk)
    if request.method == 'POST':
        review_form = MovieReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_tmp = review_form.save(commit=False)
            review_tmp.user = request.user
            review_tmp.save()
            context = {
                'review_tmp': review_tmp,
            }
            return redirect('movies:movie_detail', movie_pk)
    else:
        review_form = MovieReviewForm(instance=review)
    context = {
        'movie': movie,
        'review_tmp': review,
        'review_form': review_form,
    }
    return render(request, 'movies/detail.html', context)


@require_POST
def movie_review_delete(request, movie_pk, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(MovieReview, pk=review_pk)
        if request.user == review.user:
            review.delete()
    return redirect('movies:movie_detail', movie_pk)


def movie_list(request):
    movies1_start = Movie.objects.order_by('-released_date')[0]
    movies1 = Movie.objects.order_by('-released_date')[1:10]
    movies2_start = Movie.objects.order_by('-released_date')[10]
    movies2 = Movie.objects.order_by('-released_date')[11:20]
    movies3_start = Movie.objects.order_by('-released_date')[20]
    movies3 = Movie.objects.order_by('-released_date')[21:10]
    movies4_start = Movie.objects.order_by('-released_date')[30]  
    movies4 = Movie.objects.order_by('-released_date')[31:10]  
    movies5_start = Movie.objects.order_by('-released_date')[40]
    movies5 = Movie.objects.order_by('-released_date')[41:10]
    movies6_start = Movie.objects.order_by('-released_date')[50]
    movies6 = Movie.objects.order_by('-released_date')[51:10]
    context = {
        'movies1_start': movies1_start,
        'movies1': movies1,
        'movies2_start': movies2_start,
        'movies2': movies2,
        'movies3_start': movies3_start,
        'movies3': movies3,
        'movies4_start': movies4_start,
        'movies4': movies4,
        'movies5_start': movies5_start,
        'movies5': movies5,
        'movies6_start': movies6_start,
        'movies6': movies6,
    }
    return render(request, 'movies/movie_list.html', context)
