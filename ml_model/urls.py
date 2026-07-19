from django.urls import path
from . import views

urlpatterns = [
    path("", views.ml_prediction, name="ml_prediction"),
]