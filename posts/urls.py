from django.urls import path
from . import views

urlpatterns = [

    # =====================
    # POSTS
    # =====================

    path("", views.post_list, name="post_list"),

    path("add/", views.add_post, name="add_post"),

    path("view/<int:pk>/", views.post_detail, name="post_detail"),

    path("edit/<int:pk>/", views.edit_post, name="edit_post"),

    path("delete/<int:pk>/", views.delete_post, name="delete_post"),

    # =====================
    # LIKES
    # =====================

    path("likes/", views.like_list, name="like_list"),

    path("likes/add/", views.add_like, name="add_like"),

    path("likes/delete/<int:pk>/", views.delete_like, name="delete_like"),

    # =====================
    # COMMENTS
    # =====================

    path("comments/", views.comment_list, name="comment_list"),
    path("comments/add/", views.add_comment, name="add_comment"),
    path("comments/edit/<int:pk>/", views.edit_comment, name="edit_comment"),
    path("comments/delete/<int:pk>/", views.delete_comment, name="delete_comment"),

]