from django.urls import path
from . import views


urlpatterns = [
    path('', views.community_create),
    path('<int:community_pk>/', views.community_delete),
]
