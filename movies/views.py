from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Movie, MovieReview
from .forms import MovieReviewForm
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
@require_http_methods(['GET', 'POST'])
def main(request):
    context= {
    }
    return render(request, 'main.html', context)

@require_safe
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review_form = MovieReviewForm()
    reviews = movie.moviereview_set.order_by('-pk')
    context = {
        'movie': movie,
        'review_form': review_form,
        'reviews': reviews,
    }
    return render(request, 'movies/detail.html', context)


@require_POST
def movie_review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user.is_authenticated:
        review_form = MovieReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
    return redirect('movies:movie_detail', movie.pk)


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

# -----------------------tmdb API-----------------------
# tmdb??? ???????????? ???????????? ?????? ??????
import requests

class TMDBHelper:
    def __init__(self, api_key=None):
        self.api_key = api_key
    # url ????????????
    def get_request_url(self, method, **kwargs):
        base_url = 'https://api.themoviedb.org/3'
        request_url = base_url + method
        request_url += f'?api_key={self.api_key}'

        for k, v in kwargs.items():
            request_url += f'&{k}={v}'

        return request_url
    # ?????? ?????? ???????????? id??? ????????????
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

@require_safe
# ?????? ??????(?????? ?????? ????????? ?????? ?????? Local DB ??????)
def movie_list(request):
    # tmdb API??? ???????????? ?????? ?????? (????????? ???????????? ????????? ?????????????????? ?????? ????????????)
    # url = tmdb_helper.get_request_url('/movie/top_rated',region='KR', language='ko')
    # data = requests.get(url).json()
    # movies = []
    
    # genres_url = tmdb_helper.get_request_url('/genre/movie/list', region='KR', language='ko')
    # genres_list = requests.get(genres_url).json()
    # if 'results' in data : 
    #     for i in range(1, 11):
    #         tmp_url = url + '&page=' + str(i)
    #         movies_json = requests.get(tmp_url).json()
    #         for movie in movies_json['results']:
    #             movies.append(movie)
       
    #     genres_url = tmdb_helper.get_request_url('/genre/movie/list', region='KR', language='ko')
    #     genres_list = requests.get(genres_url).json()
    #     genres = genres_list['genres']
    #     for movie in movies:
    #         for i in range(len(movie['genre_ids'])):
    #             for j in range(len(genres)):
    #                 if movie['genre_ids'][i] == genres[j]['id']:
    #                     movie['genre_ids'][i] = genres[j]['name']
    #         data_results_start = data['results'][0]
    #         data_results_end = data['results'][1:]
    #         paginator = Paginator(movies, 10)
    #         page = request.GET.get('page')
    #         paginators = paginator.get_page(page)
    #     context = {
    #         'paginators': paginators,
    #         'movies': movies,
    #         'movie_start': data_results_start,
    #         'movie_end': data_results_end,
    #         'page_name': '?????? ??????'
    #     }
    #     return render(request, 'movies/tmdb_list_form.html', context)
    # else:
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
        'page_name': '?????? ??????'
    }
    return render(request, 'movies/movie_list.html', context)

@require_safe
# ?????? ?????? ??????
def tmdb_upcoming(request):
    url = tmdb_helper.get_request_url('/movie/upcoming',region='KR', language='ko')
    data = requests.get(url).json()
    if 'results' in data : 
        data_results = data['results']
        genres_url = tmdb_helper.get_request_url('/genre/movie/list', region='KR', language='ko')
        # url??? ????????? ????????? ??????
        genres_list = requests.get(genres_url).json()
        genres = genres_list['genres']
        # ?????? id??? name?????? ??????
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
        'page_name': '?????? ?????? ??????'
    }
    return render(request, 'movies/tmdb_list_form.html', context)


# def tmdb_toprate(request):
# ?????? ????????? index ???????????? ??????
@require_safe
def movie_index(request):
    url = tmdb_helper.get_request_url('/movie/top_rateds',region='KR', language='ko')
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
        'page_name': '?????????',
        'tmdb': 1,
        }
        return render(request, 'movies/recommend_tmdb.html', context)
    # url??? ????????? ????????? ??????????????? ??????????????? ?????? Local DB??? ??????
    else:
        data_results = Movie.objects.order_by('-vote_average')[:10]    
    
        context = {
            'movies': data_results,
            'page_name': '?????????'
        }
        return render(request, 'movies/index.html', context)


@require_safe
# ?????? ?????????
def tmdb_popular(request):
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
        'page_name': '?????? ??????',
        'tmdb': 1,
        }
        return render(request, 'movies/recommend_tmdb.html', context)

    # url??? ????????? ????????? ??????????????? ??????????????? ?????? ???????????? ??????(??????????????? ??????)
    else:      
        context = {
            'movies': '',
            'page_name': '?????? ??????'
        }
        return render(request, 'movies/index.html', context)


@require_safe
# ?????? ?????????
def tmdb_now_playing(request):
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
        'page_name': '?????? ?????? ?????? ??????'
    }
    return render(request, 'movies/tmdb_list_form.html', context)


@require_safe
# ????????????
def tmdb_search(request):
    # input??? ????????? ???
    title = request.GET.get('search')
    # ????????? ?????? url??? ??????
    url = tmdb_helper.get_request_url('/search/movie',region='KR', language='ko', query = title)
    movies = requests.get(url).json()
    context = {
        'movies': movies['results'],
    }
    return render(request,'movies/search.html',context)


@require_safe
# tmdb ?????? ????????????
def tmdb_detail(request, movie_id):
    url = tmdb_helper.get_request_url(f'/movie/{movie_id}',region='KR', language='ko')

    movie = requests.get(url).json()
    movie_genre = []

    if 'genres' in movie: 
        for genre in movie['genres'] :
            movie_genre.append(genre['name'])
        
        movie['genres'] = movie_genre
    context = {
        'movie': movie,
    }
    return render(request,'movies/tmdb_detail.html',context)


@require_safe
# ?????? ?????? ????????? ????????? ?????? ??????
def ranked_similar(request, movie_id):
    url = tmdb_helper.get_request_url(f'/movie/{movie_id}/similar',region='KR', language='ko')
    ranked_movie_url = tmdb_helper.get_request_url(f'/movie/{movie_id}',region='KR', language='ko')
    data = requests.get(url).json()
    ranked_movie = requests.get(ranked_movie_url).json()
    if 'results' in data : 
        movies= data['results']
        genres_url = tmdb_helper.get_request_url('/genre/movie/list', region='KR', language='ko')
        genres_list = requests.get(genres_url).json()
        genres = genres_list['genres']
        for movie in movies:
            for i in range(len(movie['genre_ids'])):
                for j in range(len(genres)):
                    if movie['genre_ids'][i] == genres[j]['id']:
                        movie['genre_ids'][i] = genres[j]['name']
        data_results_start = data['results'][0]
        data_results_end = data['results'][1:]
        paginator = Paginator(movies, 10)
        page = request.GET.get('page')
        paginators = paginator.get_page(page)
    else:
        data_results_start = ''
        data_results_end = ''
        paginators = ''
        movies = ''
    context = {
        'paginators': paginators,
        'movies': movies,
        'ranked_movie': ranked_movie,
        'movie_start': data_results_start,
        'movie_end': data_results_end,
        'page_name': '????????? ????????? ????????? ??????'
    }
    return render(request, 'movies/ranked_similar.html', context)

# ?????? ?????? ?????? ??????
def rank_list(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    movies_tmp = person.moviereview_set.all()
    movie_ids = []
    movies = []
    for movie in movies_tmp :
        movie_ids.append(movie.movie.movie_id)
    movie_ids = set(movie_ids)
    for movie_id in movie_ids:
        movie = Movie.objects.get(movie_id=movie_id)
        movies.append(movie)
    context = {
        'person': person,
        # 'movie_ids': movie_ids,
        'movies': movies, 
    }
    return render(request, 'movies/rank_list.html', context)

# ------------------- Face Recognization -------------------
import json
import requests
import datetime


@require_safe
def face_recommends(request):
    client_id = "nSNNt9Iyb9ef1PxjBLPF"
    client_secret = "yjeOVJx1Qz"

    url = "https://openapi.naver.com/v1/vision/face"
    
    # ?????? ??????
    if not request.user.profile_img :
        gender = 'None'
        age_average = 'None'
    else:
        files = {'image': request.user.profile_img }
        headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
        response = requests.post(url,  files=files, headers=headers)
        result = json.loads(response.text)
        if not 'faces' in result:
            return render(request, 'movies/face_recommends.html')
        # ?????? ??????
        if result['faces'] == []:
            gender = 'None'
            age_average = 'None'
        elif result['faces'][0]['gender']['value'] == 'male':
            gender = '??????'
            age_front = int(result['faces'][0]['age']['value'].split('~')[0])
            age_end = int(result['faces'][0]['age']['value'].split('~')[1])
            age_average = int((age_front + age_end) / 2)
        else:
            gender = '??????'
            age_front = int(result['faces'][0]['age']['value'].split('~')[0])
            age_end = int(result['faces'][0]['age']['value'].split('~')[1])
            age_average = int((age_front + age_end) / 2)

    url = tmdb_helper.get_request_url('/movie/top_rated',region='KR', language='ko')
    datas, movies = [], []
    for i in range(1,6):
        tmp_url = url + '&page=' + str(i)
        data = requests.get(tmp_url).json()
        datas.append(data['results'])
        movies += datas[i-1]
    genres_url = tmdb_helper.get_request_url('/genre/movie/list', region='KR', language='ko')
    genres_list = requests.get(genres_url).json()
    genres = genres_list['genres']
    for movie in movies:
        for i in range(len(movie['genre_ids'])):
            for j in range(len(genres)):
                if movie['genre_ids'][i] == genres[j]['id']:
                    movie['genre_ids'][i] = genres[j]['name']
    # 20??? ????????? ?????? adult=True??? ?????? ?????????
    # 20~29??? ???????????? release_date ??? 2015??? ????????? ?????? ??????
    # 30??? ?????? ???????????? release_date ??? 2015??? ????????? ?????? ??????
    # ?????? ????????? ????????? ?????? ????????? ??????
    
    filter_movies = []
    if age_average == 'None':
        pass
    elif age_average < 20:
        for i in range(len(movies)):
            if movies[i]['adult'] == False:
                if 2020 <= int(movies[i]['release_date'][:4]):
                    filter_movies.append(movies[i])
                else:
                    continue
        if len(filter_movies) < 10:
            pass
        else:
            filter_movies = filter_movies[:10]

    elif 20 <= age_average < 30:
        for i in range(len(movies)):
            if 2010 <= int(movies[i]['release_date'][:4]) <= 2019:
                filter_movies.append(movies[i])
            else:
                continue
        if len(filter_movies) < 10:
            pass
        else:
            filter_movies = filter_movies[:10]

    elif 30 <= age_average < 40:
        for i in range(len(movies)):
            if 2000 <= int(movies[i]['release_date'][:4]) <= 2009:
                filter_movies.append(movies[i])
            else:
                continue
        if len(filter_movies) < 10:
            pass
        else:
            filter_movies = filter_movies[:10]

    else:
        for i in range(len(movies)):
            if int(movies[i]['release_date'][:4]) <= 1999:
                filter_movies.append(movies[i])
            else:
                continue
        if len(filter_movies) < 10:
            pass
        else:
            filter_movies = filter_movies[:10]

    context = {
        'movies': filter_movies,
        'gender': gender,
        'age_average': age_average,
        'page_name': '???????????? ?????? ??????',
    }
    return render(request, 'movies/face_recommends.html', context)

import random
@require_safe
# ?????? ?????? ?????? ??????
def genre_recommends(request, genre_ids):
    url = tmdb_helper.get_request_url(f'/movie/popular',region='KR', language='ko')
    movies = []
    if genre_ids == 0:
        # ?????? ????????? ??????id??? 0?????? ??????
        pass
    else: 
        for i in range(1, 11):
            tmp_url = url + '&page=' + str(i)
            movies_json = requests.get(tmp_url).json()
            for movie in movies_json['results']:
                if genre_ids in movie['genre_ids']:
                    movies.append(movie)
    # ????????? ????????? ?????? ????????? ?????? 0, 1, 2, 3, 4(??????)?????? ???????????? ??????
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