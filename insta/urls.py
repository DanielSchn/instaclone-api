from django.urls import path
from .views import InstagramView, PostListView, like_post, get_posts_with_like, submit_comment, get_single_comments, get_users, create_post

urlpatterns = [
    path('', InstagramView.as_view()),
    path('user/<int:pk>', InstagramView.as_view()),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('like-post/', like_post, name='like_post'),
    path('get-posts-with-like/', get_posts_with_like, name="get_posts_with_like"),
    path('submit-comment/', submit_comment, name='submit-comment'),
    path('get-comments/<int:post_id>/', get_single_comments, name='get_comments'),
    path('get-users/', get_users, name='get-users'),
    path('create-post/', create_post, name='create-post')
]
