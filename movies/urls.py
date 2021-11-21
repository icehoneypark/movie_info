from django.urls import path
from . import views

app_name="movies"
urlpatterns = [
    path('', views.movie_index, name='movie_index'),
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_pk>/reviews/<int:review_pk>/update/', views.movie_review_update, name='movie_review_update'),
    path('<int:movie_pk>/reviews/<int:review_pk>/delete/', views.movie_review_delete, name='movie_review_delete'),
    path('<int:movie_pk>/reviews/create/', views.movie_review_create, name='movie_review_create'),
]