from django.contrib import admin
from .models import Comment, Like, Post, User

class UserAdmin(admin.ModelAdmin):
    list_filter = ['username']
    list_display = ['username', 'email_address']

class PostAdmin(admin.ModelAdmin):
    list_filter = ['user', 'created_at']
    list_display = ['user', 'created_at']

class LikeAdmin(admin.ModelAdmin):
    list_filter = ['user', 'post', 'created_at']
    list_display = ['user', 'post', 'created_at']

class CommentAdmin(admin.ModelAdmin):
    list_filter = ['user', 'post', 'created_at']
    list_display = ['user', 'post', 'created_at']

# Register your models here.
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(User, UserAdmin)