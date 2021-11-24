from django.urls import path
from . import views

app_name="movies"
urlpatterns = [
    path('', views.movie_index, name='movie_index'),
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_pk>/reviews/<int:review_pk>/update/', views.movie_review_update, name='movie_review_update'),
    path('<int:movie_pk>/reviews/<int:review_pk>/delete/', views.movie_review_delete, name='movie_review_delete'),
    path('<int:movie_pk>/reviews/create/', views.movie_review_create, name='movie_review_create'),
    path('list/', views.movie_list, name='movie_list'),
    # tmdb
    path('tmdb_upcoming/', views.tmdb_upcoming, name="tmdb_upcoming"),
    path('tmdb_popular/', views.tmdb_popular, name="tmdb_popular"),
    path('tmdb_now_playing/', views.tmdb_now_playing, name="tmdb_now_playing"),
    path('face_recommends/', views.face_recommends, name="face_recommends"),
    path('tmdb_search/', views.tmdb_search, name="tmdb_search"),
    path('tmdb_detail/<int:movie_id>/', views.tmdb_detail, name="tmdb_detail"),
    path('genre_recommends/<int:genre_ids>/', views.genre_recommends, name="genre_recommends"),
    path('<int:movie_id>/similar', views.ranked_similar, name="ranked_similar"),    
    path('<str:username>/rank_list/', views.rank_list, name='rank_list'),
]