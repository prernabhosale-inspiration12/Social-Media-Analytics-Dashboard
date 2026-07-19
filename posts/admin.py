from django.contrib import admin
from .models import Post, Like, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "department",
        "caption",
        "created_at",
    )

    list_filter = (
        "department",
        "created_at",
    )

    search_fields = (
        "caption",
        "user__username",
        "department__department_name",
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "post",
        "liked_at",
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "post",
        "comment",
        "commented_at",
    )

    search_fields = (
        "comment",
    )