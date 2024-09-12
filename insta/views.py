from django.http import JsonResponse
from .models import User, Post, Like, Comment
from django.views.generic.base import RedirectView
from django.views import View
import json
# Create your views here.


class InstagramView(RedirectView):
    permanent = True
    url = 'posts/'


class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().prefetch_related('comments', 'likes', 'user')
        post_list = []
        for post in posts:
            post_data = {
                "username": post.user.username,
                "profile_image": post.user.profile_image.url,
                "location": post.location,
                "image": post.image.url,
                "created_at": post.created_at.strftime('%Y-%m-%d %H:%M'),
                "likes_count": post.likes.count(),
                "description": post.description,
                "post_id": post.id,
                "comments": [
                    {
                        "username": comment.user.username,
                        "content": comment.content,
                        "created_at": comment.created_at.strftime('%Y-%m-%d %H:%M'),
                    } for comment in post.comments.all()
                ],
            }
            post_list.append(post_data)
        return JsonResponse(post_list, safe=False)


def like_post(request):
    try:
        data = json.loads(request.body)
        post_id = data.get('post_id')
        user_id = User.objects.first().id
        post = Post.objects.get(id=post_id)
        user = User.objects.get(id=user_id)
        result = get_or_delete(post)
        if result['deleted']:
            return JsonResponse({"success": True})
        else:
            Like.objects.create(post=post, user=user)
            return JsonResponse({"success": True})
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})


def get_or_delete(post):
    try:
        user = User.objects.first()
        like = Like.objects.get(post=post, user=user)
        like.delete()
        return {"deleted": True}
    except Like.DoesNotExist:
        return {"deleted": False}


def get_posts_with_like(request):
    try:
        user = User.objects.first()
        posts = Post.objects.all()
        likes = Like.objects.filter(
            user=user).values_list('post_id', flat=True)
        posts_with_likes = [
            {
                "id": post.id,
                "liked": post.id in likes
            }
            for post in posts
        ]
        return JsonResponse({"posts": posts_with_likes})
    except Exception as e:
        return JsonResponse({"success": False, "error": e})


def submit_comment(request):
    try:
        data = json.loads(request.body)
        post_id = data.get('post_id')
        comment_text = data.get('comment')
        username = data.get('user')
        user = User.objects.get(username=username)
        post = Post.objects.get(id=post_id)
        Comment.objects.create(
            post=post, user=user, content=comment_text)

        return JsonResponse({"success": True})
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})


def get_single_comments(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        comments = Comment.objects.filter(post=post).select_related('user')
        comments_list = [
            {
                "user": comment.user.username,
                "content": comment.content
            }
            for comment in comments
        ]

        return JsonResponse({"comments": comments_list})
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})


def get_users(request):
    try:
        users = User.objects.all()
        users_list = [
            {
                "id": user.id,
                "name": user.username
            } for user in users
        ]
        return JsonResponse({"users": users_list})
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})


def create_post(request):
    try:
        user_id = request.POST.get('user')
        location = request.POST.get('location')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        user = User.objects.get(id=user_id)

        new_post = Post.objects.create(
            user=user,
            location=location,
            description=description,
            image=image
        )
        return JsonResponse({"success": True})

    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})