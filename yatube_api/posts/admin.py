from django.contrib import admin

from .models import Comment, Follow, Group, Post

EMPTY = '-пусто-'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'author', 'image', 'pk')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = EMPTY


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'post', 'author', 'created')
    search_fields = ('text',)
    empty_value_display = EMPTY


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following')
    search_fields = ('user',)
    empty_value_display = EMPTY


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description', 'pk')
    search_fields = ('title',)
    empty_value_display = EMPTY
