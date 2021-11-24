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

# def movie_index(request):
    
#     movies = Movie.objects.order_by('-popularity')[:10]
#     context = {
#         'movies': movies,
#         'page_name': '관객수',
#     }
#     return render(request, 'movies/index.html', context)

# def movie_index(request):
    
#     # movies = Movie.objects.order_by('-popularity')
#     top_1 = Movie.objects.order_by('-popularity')[0]
#     top_2 = Movie.objects.order_by('-popularity')[1]
#     top_3 = Movie.objects.order_by('-popularity')[2]
#     top_4 = Movie.objects.order_by('-popularity')[3]
#     top_5 = Movie.objects.order_by('-popularity')[4]
#     top_6 = Movie.objects.order_by('-popularity')[5]
#     top_7 = Movie.objects.order_by('-popularity')[6]
#     top_8 = Movie.objects.order_by('-popularity')[7]
#     top_9 = Movie.objects.order_by('-popularity')[8]
#     top_10 = Movie.objects.order_by('-popularity')[9]
#     context = {
#         # 'movies': movies,
#         'top1': top_1,
#         'top2': top_2,
#         'top3': top_3,
#         'top4': top_4,
#         'top5': top_5,
#         'top6': top_6,
#         'top7': top_7,
#         'top8': top_8,
#         'top9': top_9,
#         'top10': top_10,
#     }
#     return render(request, 'movies/index.html', context)

@require_safe
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review_form = MovieReviewForm()
    reviews = movie.moviereview_set.order_by('-pk')
    # date_str1 = movie.release_date#[0]
    # date_str2 = movie.release_date#[1]
    # date_str3 = movie.release_date#[2]
    # date_str4 = movie.release_date#[3]
    # date_str5 = movie.release_date#[5]
    # date_str6 = movie.release_date#[6]
    # date_str7 = movie.release_date#[8]
    # date_str8 = movie.release_date#[9]
    context = {
        'movie': movie,
        'review_form': review_form,
        'reviews': reviews,
        # 'date_str1': date_str1,
        # 'date_str2': date_str2,
        # 'date_str3': date_str3,
        # 'date_str4': date_str4,
        # 'date_str5': date_str5,
        # 'date_str6': date_str6,
        # 'date_str7': date_str7,
        # 'date_str8': date_str8,
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
    movies_1 = Movie.objects.order_by('-release_date')[1:60] 
    movies1_start = Movie.objects.order_by('-release_date')[0]
    
    movies = Movie.objects.order_by('-release_date')
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
    if 'results' in data : 
        data_results = data['results']
        genres_url = tmdb_helper.get_request_url('/genre/movie/list', region='KR', language='ko')
        genres_list = requests.get(genres_url).json()
        genres = genres_list['genres']
        for movie in data_results:
            for i in range(len(movie['genre_ids'])):
                for j in range(len(genres)):
                    if movie['genre_ids'][i] == genres[j]['id']:
                        movie['genre_ids'][i] = genres[j]['name']
        data_results_start = data['results'][0]
        data_results_end = data['results'][1:]

        paginator = Paginator(data_results, 10)
        page = request.GET.get('page')
        paginators = paginator.get_page(page)
    else:
        data_results_start = ''
        data_results_end = ''
        paginators = ''
        data_results = ''
    context = {
        'paginators': paginators,
        'movies': data_results,
        'movie_start': data_results_start,
        'movie_end': data_results_end,
        'page_name': '개봉 예정 영화'
    }
    return render(request, 'movies/tmdb_list_form.html', context)


# def tmdb_toprate(request):
    
def movie_index(request):
    # 개봉예정 url = '/movie/upcoming' (필요한 내용에 대한 url을 수정하면 됨)
    url = tmdb_helper.get_request_url('/movie/top_rated',region='KR', language='ko')
    data = requests.get(url).json()
    if 'results' in data : 
        data_results = data['results'][:10]
        genres_url = tmdb_helper.get_request_url('/genre/movie/list', region='KR', language='ko')
        genres_list = requests.get(genres_url).json()
        genres = genres_list['genres']
        for movie in data_results:
            for i in range(len(movie['genre_ids'])):
                for j in range(len(genres)):
                    if movie['genre_ids'][i] == genres[j]['id']:
                        movie['genre_ids'][i] = genres[j]['name']
        context = {
        'movies': data_results,
        'page_name': '평점순',
        'tmdb': 1,
        }
        return render(request, 'movies/recommend_tmdb.html', context)

    else:
        data_results = Movie.objects.order_by('-vote_average')[:10]    
    
        context = {
            'movies': data_results,
            'page_name': '평점순'
        }
        return render(request, 'movies/index.html', context)

def tmdb_popular(request):
    # 개봉예정 url = '/movie/upcoming' (필요한 내용에 대한 url을 수정하면 됨)
    url = tmdb_helper.get_request_url('/movie/popular',region='KR', language='ko')
    data = requests.get(url).json()
    if 'results' in data : 
        data_results = data['results'][:10]
        genres_url = tmdb_helper.get_request_url('/genre/movie/list', region='KR', language='ko')
        genres_list = requests.get(genres_url).json()
        genres = genres_list['genres']
        for movie in data_results:
            for i in range(len(movie['genre_ids'])):
                for j in range(len(genres)):
                    if movie['genre_ids'][i] == genres[j]['id']:
                        movie['genre_ids'][i] = genres[j]['name']
        context = {
        'movies': data_results,
        'page_name': '인기 영화',
        'tmdb': 1,
        }
        return render(request, 'movies/recommend_tmdb.html', context)

    else:  
    
        context = {
            'movies': '',
            'page_name': '인기 영화'
        }
        return render(request, 'movies/index.html', context)

def tmdb_now_playing(request):
    # 개봉예정 url = '/movie/upcoming' (필요한 내용에 대한 url을 수정하면 됨)
    url = tmdb_helper.get_request_url('/movie/now_playing',region='KR', language='ko')
    data = requests.get(url).json()
    if 'results' in data : 
        data_results = data['results']
        genres_url = tmdb_helper.get_request_url('/genre/movie/list', region='KR', language='ko')
        genres_list = requests.get(genres_url).json()
        genres = genres_list['genres']
        for movie in data_results:
            for i in range(len(movie['genre_ids'])):
                for j in range(len(genres)):
                    if movie['genre_ids'][i] == genres[j]['id']:
                        movie['genre_ids'][i] = genres[j]['name']
        data_results_start = data['results'][0]
        data_results_end = data['results'][1:]
        paginator = Paginator(data_results, 10)
        page = request.GET.get('page')
        paginators = paginator.get_page(page)
    else:
        data_results_start = ''
        data_results_end = ''
        paginators = ''
        data_results = ''
    context = {
        'paginators': paginators,
        'movies': data_results,
        'movie_start': data_results_start,
        'movie_end': data_results_end,
        'page_name': '현재 상영 중인 영화'
    }
    return render(request, 'movies/tmdb_list_form.html', context)

def tmdb_search(request):
    title = request.GET.get('search')
    url = tmdb_helper.get_request_url('/search/movie',region='KR', language='ko', query = title)
    movies = requests.get(url).json()
    context = {
        'movies': movies['results'],
    }
    return render(request,'movies/search.html',context)


def tmdb_detail(request, movie_id):
    url = tmdb_helper.get_request_url(f'/movie/{movie_id}',region='KR', language='ko')

    movie = requests.get(url).json()
    movie_genre = []

    if 'genres' in movie: 
        for genre in movie['genres'] :
            # print(genre['name'])
            movie_genre.append(genre['name'])
        
        movie['genres'] = movie_genre
    context = {
        'movie': movie,
    }
    return render(request,'movies/tmdb_detail.html',context)

# ------------------- Face Recognization -------------------
import json
import requests
import datetime
def face_recommends(request):
    client_id = "nSNNt9Iyb9ef1PxjBLPF"
    client_secret = "yjeOVJx1Qz"

    url = "https://openapi.naver.com/v1/vision/face"

    if not request.user.profile_img :
        gender = 'None'
        age_average = 'None'
    else:
        files = {'image': request.user.profile_img }
        headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
        response = requests.post(url,  files=files, headers=headers)
        result = json.loads(response.text)
        if result['faces'] == []:
            gender = 'None'
            age_average = 'None'
        elif result['faces'][0]['gender']['value'] == 'male':
            gender = '남자'
            age_front = int(result['faces'][0]['age']['value'].split('~')[0])
            age_end = int(result['faces'][0]['age']['value'].split('~')[1])
            age_average = int((age_front + age_end) / 2)
        else:
            gender = '여자'
            age_front = int(result['faces'][0]['age']['value'].split('~')[0])
            age_end = int(result['faces'][0]['age']['value'].split('~')[1])
            age_average = int((age_front + age_end) / 2)

    url = tmdb_helper.get_request_url('/movie/top_rated',region='KR', language='ko')
    data = requests.get(url).json()
    movies = data['results']
    movies[0]['tmp'] = 1
    genres_url = tmdb_helper.get_request_url('/genre/movie/list', region='KR', language='ko')
    genres_list = requests.get(genres_url).json()
    genres = genres_list['genres']
    for movie in movies:
        for i in range(len(movie['genre_ids'])):
            for j in range(len(genres)):
                if movie['genre_ids'][i] == genres[j]['id']:
                    movie['genre_ids'][i] = genres[j]['name']

    # 20세 미만의 경우 adult=True인 영화 필터링
    # 20~29세 이용자는 release_date 가 2015년 이후인 영화 추천
    # 30세 이상 이용자는 release_date 가 2015년 이전인 영화 추천
    # 얼굴 인식이 안되는 경우 메시지 출력
    if age_average == 'None':
        rec_movie = []
        carousel_movies = []
    elif 20 <= age_average < 30:
        rec_movie = Movie.objects.filter(release_date__gte=datetime.date(2010, 1, 1)).filter(release_date__lte=datetime.date(2019, 12, 31))
        carousel_movies = rec_movie[:10]

    elif age_average < 20:
        rec_movie = Movie.objects.filter(adult=False).filter(release_date__gte=datetime.date(2020, 1, 1))
        carousel_movies = rec_movie[:10]

    elif 30 <= age_average < 40:
        rec_movie = Movie.objects.filter(release_date__gte=datetime.date(2000, 1, 1)).filter(release_date__lte=datetime.date(2009, 12, 31))
        carousel_movies = rec_movie[:10]

    else:
        rec_movie = Movie.objects.filter(release_date__lte=datetime.date(1999, 12, 31))
        carousel_movies = rec_movie[:10]

    
    paginator = Paginator(rec_movie, 10)
    page = request.GET.get('page')
    paginators = paginator.get_page(page)

    context = {
        'carousel_movies': carousel_movies,
        'movies': rec_movie,
        'gender': gender,
        'age_average': age_average,
        'paginators': paginators,
        'page_name': '연령대별 추천 영화',
    }
    return render(request, 'movies/face_recommends.html', context)

import random

def genre_recommends(request, genre_ids):
    url = tmdb_helper.get_request_url(f'/movie/popular',region='KR', language='ko')
    movies = []
    if genre_ids == 0:
        pass
    else: 
        for i in range(1, 11):
            tmp_url = url + '&page=' + str(i)        
            print(tmp_url)
            movies_json = requests.get(tmp_url).json()
            for movie in movies_json['results']:
                if genre_ids in movie['genre_ids']:
                    movies.append(movie)
    if len(movies) == 0:
        context = {
            'movies': [],
            'genre': genre_ids
        }
    elif len(movies) == 1:        
        context = {
            'movies': random.sample(movies, 1)
        }
    elif len(movies) == 2:        
        context = {
            'movies': random.sample(movies, 2)
        }
    elif len(movies) == 3:        
        context = {
            'movies': random.sample(movies, 3)
        }
    else :
        context = {
            'movies': random.sample(movies, 4)
        }    
    return render(request, 'movies/genre_recommends.html/', context)