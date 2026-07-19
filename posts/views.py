
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.models import User

from .models import Post, Like, Comment
from .forms import PostForm, LikeForm, CommentForm
from django.contrib import messages


# ==========================
# Post List
# ==========================

def post_list(request):

    search = request.GET.get("search", "")

    posts = Post.objects.select_related(
        "department",
        "user"
    ).order_by("-created_at")

    if search:
        posts = posts.filter(
            Q(caption__icontains=search) |
            Q(department__department_name__icontains=search) |
            Q(user__username__icontains=search)
        )

    paginator = Paginator(posts, 5)

    page = request.GET.get("page")

    posts = paginator.get_page(page)

    return render(
        request,
        "posts/post_list.html",
        {
            "posts": posts,
            "search": search,
        }
    )
# ==========================
# Add Post
# ==========================

def add_post(request):

    if request.method == "POST":

        form = PostForm(

            request.POST,

            request.FILES

        )

        if form.is_valid():

            post = form.save(commit=False)

            post.user = User.objects.first()

            post.save()

            messages.success(

                request,

                "Post created successfully."

            )

            return redirect("post_list")

    else:

        form = PostForm()

    return render(

        request,

        "posts/add_post.html",

        {

            "form": form

        }

    )


# ==========================
# Edit Post
# ==========================

def edit_post(request, pk):

    post = get_object_or_404(

        Post,

        pk=pk

    )

    if request.method == "POST":

        form = PostForm(

            request.POST,

            request.FILES,

            instance=post

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Post updated successfully."

            )

            return redirect("post_list")

    else:

        form = PostForm(

            instance=post

        )

    return render(

        request,

        "posts/edit_post.html",

        {

            "form": form

        }

    )


# ==========================
# Delete Post
# ==========================

def delete_post(request, pk):

    post = get_object_or_404(

        Post,

        pk=pk

    )

    post.delete()

    messages.success(

        request,

        "Post deleted successfully."

    )

    return redirect("post_list")


# ==========================
# Post Detail
# ==========================

def post_detail(request, pk):

    post = get_object_or_404(

        Post,

        pk=pk

    )

    return render(

        request,

        "posts/post_detail.html",

        {

            "post": post

        }

    )
# ==========================
# LIKE MODULE
# ==========================

def like_list(request):

    likes = Like.objects.select_related(
        "user",
        "post"
    ).all()

    context = {
        "likes": likes
    }

    return render(
        request,
        "likes/like_list.html",
        context
    )


def add_like(request):

    if request.method == "POST":

        form = LikeForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Like Added Successfully!"
            )

            return redirect("like_list")

    else:

        form = LikeForm()

    return render(
        request,
        "likes/add_like.html",
        {"form": form}
    )
# ==========================
# Delete Like
# ==========================

def delete_like(request, pk):

    like = get_object_or_404(
        Like,
        pk=pk
    )

    like.delete()

    messages.success(
        request,
        "Like deleted successfully."
    )

    return redirect("like_list")
# ==========================
# COMMENT MODULE
# ==========================

def comment_list(request):

    search = request.GET.get("search", "")

    comments = Comment.objects.select_related(
        "user",
        "post"
    ).order_by("-commented_at")

    if search:

        comments = comments.filter(
            Q(user__username__icontains=search) |
            Q(post__caption__icontains=search) |
            Q(comment__icontains=search)
        )

    paginator = Paginator(comments, 5)

    page = request.GET.get("page")

    comments = paginator.get_page(page)

    return render(
        request,
        "comments/comment_list.html",
        {
            "comments": comments,
            "search": search,
        }
    )
# ==========================
# Add Comment
# ==========================

def add_comment(request):

    if request.method == "POST":

        form = CommentForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Comment Added Successfully!"
            )

            return redirect("comment_list")

    else:

        form = CommentForm()

    return render(
        request,
        "comments/add_comment.html",
        {
            "form": form
        }
    )

# ==========================
# Edit Comment
# ==========================

def edit_comment(request, pk):

    comment = get_object_or_404(
        Comment,
        pk=pk
    )

    if request.method == "POST":

        form = CommentForm(
            request.POST,
            instance=comment
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Comment updated successfully."
            )

            return redirect("comment_list")

    else:

        form = CommentForm(
            instance=comment
        )

    return render(
        request,
        "comments/edit_comment.html",
        {
            "form": form
        }
    )

# ==========================
# Delete Comment
# ==========================

def delete_comment(request, pk):

    comment = get_object_or_404(
        Comment,
        pk=pk
    )

    comment.delete()

    messages.success(
        request,
        "Comment deleted successfully."
    )

    return redirect("comment_list")