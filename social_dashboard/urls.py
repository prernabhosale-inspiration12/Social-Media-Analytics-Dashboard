"""
URL configuration for social_dashboard project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from analytics_app.views import analytics_dashboard

urlpatterns = [

    path(
        "admin/",
        admin.site.urls
    ),

    path(
        "",
        analytics_dashboard,
        name="dashboard"
    ),

    path(
        "departments/",
        include("departments.urls")
    ),

    path(
        "posts/",
        include("posts.urls")
    ),

    path(
        "ml/",
        include("ml_model.urls")
    ),

    path(
        "analytics/",
        include("analytics_app.urls")
    ),
    path(
    "accounts/",
    include("accounts.urls")
),
    path(
    "reports/",
    include("reports.urls")
),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )