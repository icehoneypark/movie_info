from django.urls import path
from . import views

app_name="movies"
urlpatterns = [
    path('', views.movie_index, name='movie_index'),
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('list/', views.movie_list, name='movie_list'),
]