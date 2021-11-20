from django.urls import path
from . import views

app_name="community"
urlpatterns = [
    path('', views.community_index, name='community_index'),
    path('create/', views.community_create, name='community_create'),
    path('<int:post_pk>/', views.community_detail, name='community_detail'),
    path('<int:pk>/update/', views.community_update, name='community_update'),
    path('<int:pk>/delete/', views.community_delete, name='community_delete'),
    path('<int:post_pk>/comments/<int:comment_pk>/update/', views.community_comment_update, name='community_comment_update'),
    path('<int:post_pk>/comments/<int:comment_pk>/delete/', views.community_comment_delete, name='community_comment_delete'),
    path('<int:post_pk>/comments/create/', views.community_comment_create, name='community_comment_create'),
]