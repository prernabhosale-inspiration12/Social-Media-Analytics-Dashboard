from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.db.models.functions import ExtractMonth

from posts.models import Post, Like, Comment
from departments.models import Department


@login_required(login_url="login")
def analytics_dashboard(request):

    users = User.objects.count()
    posts = Post.objects.count()
    likes = Like.objects.count()
    comments = Comment.objects.count()

    # Search & Filter
    search = request.GET.get("search", "")
    department = request.GET.get("department", "")

    recent_posts = (
        Post.objects
        .select_related("user", "department")
    )

    if search:
        recent_posts = recent_posts.filter(
            Q(caption__icontains=search) |
            Q(user__username__icontains=search)
        )

    if department:
        recent_posts = recent_posts.filter(
            department__id=department
        )

    recent_posts = recent_posts.order_by("-created_at")[:10]

    departments = Department.objects.all()
    

    # Department Chart
    department_queryset = (
        Department.objects
        .annotate(total_posts=Count("post"))
        .order_by("department_name")
    )

    department_names = [
        d.department_name
        for d in department_queryset
    ]

    department_posts = [
        d.total_posts
        for d in department_queryset
    ]

    # Top Users
    top_users_queryset = (
        User.objects
        .annotate(posts_count=Count("post"))
        .order_by("-posts_count")[:5]
    )

    max_posts = 1

    if top_users_queryset.exists():
        max_posts = top_users_queryset.first().posts_count or 1

    top_users = []

    for user in top_users_queryset:

        top_users.append({

            "name": user.username,
            "posts": user.posts_count,
            "progress": int((user.posts_count / max_posts) * 100)

        })

    # Monthly Posts
    month_names = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    monthly_queryset = (
        Post.objects
        .annotate(month=ExtractMonth("created_at"))
        .values("month")
        .annotate(total=Count("id"))
        .order_by("month")
    )

    monthly_posts = [0] * 12

    for item in monthly_queryset:

        if item["month"]:
            monthly_posts[item["month"] - 1] = item["total"]

    # Most Active Department
    most_active_department = (
        Department.objects
        .annotate(total_posts=Count("post"))
        .order_by("-total_posts")
        .first()
    )

    # Most Liked Post
    most_liked_post = (
        Post.objects
        .annotate(total_likes=Count("like"))
        .order_by("-total_likes")
        .first()
    )

    # Most Commented Post
    most_commented_post = (
        Post.objects
        .annotate(total_comments=Count("comment"))
        .order_by("-total_comments")
        .first()
    )

    context = {

        "users": users,
        "posts": posts,
        "likes": likes,
        "comments": comments,

        "recent_posts": recent_posts,

        "departments": departments,
        "search": search,

        "department_names": department_names,
        "department_posts": department_posts,

        "top_users": top_users,

        "months": month_names,
        "monthly_posts": monthly_posts,

        "most_active_department": most_active_department,
        "most_liked_post": most_liked_post,
        "most_commented_post": most_commented_post,

    }

    return render(
        request,
        "dashboard.html",
        context
    )