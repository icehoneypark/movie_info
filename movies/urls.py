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
    path('tmdb_toprate/', views.tmdb_toprate, name="tmdb_toprate"),
    path('tmdb_popular/', views.tmdb_popular, name="tmdb_popular"),
    path('tmdb_now_playing/', views.tmdb_now_playing, name="tmdb_now_playing"),
    path('tmdb_detail/', views.tmdb_search, name="tmdb_detail"),
]