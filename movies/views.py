from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Movie, MovieReview
from .forms import MovieReviewForm
from django.core.paginator import Paginator

@require_http_methods(['GET', 'POST'])
def main(request):
    context= {
    }
    return render(request, 'main.html', context)

def movie_index(request):
    movies = Movie.objects.order_by('-popularity')
    paginator = Paginator(movies, 10)
    page = request.GET.get('page')
    paginators = paginator.get_page(page)
    # top_10 = Movie.objects.order_by('-popularity')[:10]
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
        'paginators': paginators,
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
    movies_1 = Movie.objects.order_by('-released_date')[1:60] 
    movies1_start = Movie.objects.order_by('-released_date')[0]
    
    movies = Movie.objects.order_by('-released_date')
    paginator = Paginator(movies, 10)
    page = request.GET.get('page')
    paginators = paginator.get_page(page)
    context = {
        'movies_1': movies_1,
        'movies1_start': movies1_start,
        'paginators': paginators,
    }
    return render(request, 'movies/movie_list.html', context)

# -----------------------tmdb API-----------------------

import requests

class TMDBHelper:
    def __init__(self, api_key=None):
        self.api_key = api_key


    def get_request_url(self, method, **kwargs):
        base_url = 'https://api.themoviedb.org/3'
        request_url = base_url + method
        request_url += f'?api_key={self.api_key}'

        for k, v in kwargs.items():
            request_url += f'&{k}={v}'

        return request_url
    def get_movie_id(self, title):
        request_url = self.get_request_url('/search/movie', query=title, region='KR', language='ko')
        data = requests.get(request_url).json()
        results = data.get('results')
        if results:
            movie = results[0]
            movie_id = movie['id']
            return movie_id
        else:
            return None

tmdb_helper = TMDBHelper('6163fbe091536a27c8951c10ecb40d6c')

def tmdb_upcoming(request):
    # 개봉예정 url = '/movie/upcoming' (필요한 내용에 대한 url을 수정하면 됨)
    url = tmdb_helper.get_request_url('/movie/upcoming',region='KR', language='ko')
    data = requests.get(url).json()
    data_results = data['results']
    data_results[0]['tmp'] = 1
    context = {
        'movies': data_results,
        'page_name': '개봉 예정 영화'
    }
    return render(request, 'movies/tmdb_list_form.html', context)


def tmdb_toprate(request):
    # 개봉예정 url = '/movie/upcoming' (필요한 내용에 대한 url을 수정하면 됨)
    url = tmdb_helper.get_request_url('/movie/top_rated',region='KR', language='ko')
    data = requests.get(url).json()
    data_results = data['results']
    data_results[0]['tmp'] = 1
    context = {
        'movies': data_results,
        'page_name': '높은 평점 영화'
    }
    return render(request, 'movies/tmdb_list_form.html', context)

def tmdb_popular(request):
    # 개봉예정 url = '/movie/upcoming' (필요한 내용에 대한 url을 수정하면 됨)
    url = tmdb_helper.get_request_url('/movie/popular',region='KR', language='ko')
    data = requests.get(url).json()
    data_results = data['results']
    data_results[0]['tmp'] = 1
    context = {
        'movies': data_results,
        'page_name': '인기 영화'
    }
    return render(request, 'movies/tmdb_list_form.html', context)

def tmdb_now_playing(request):
    # 개봉예정 url = '/movie/upcoming' (필요한 내용에 대한 url을 수정하면 됨)
    url = tmdb_helper.get_request_url('/movie/now_playing',region='KR', language='ko')
    data = requests.get(url).json()
    data_results = data['results']
    data_results[0]['tmp'] = 1
    context = {
        'movies': data_results,
        'page_name': '현재 상영 중인 영화'
    }
    return render(request, 'movies/tmdb_list_form.html', context)

def tmdb_search(request):
    title = request.GET.get('search')
    movie_id = tmdb_helper.get_movie_id(title)
    url = tmdb_helper.get_request_url(f'/movie/{movie_id}',region='KR', language='ko')

    movie = requests.get(url).json()

    context = {
        'movie': movie,
    }
    return render(request,'movies/tmdb_detail.html',context)