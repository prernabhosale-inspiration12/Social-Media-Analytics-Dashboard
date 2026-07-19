from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.department_list,
        name="department_list"
    ),

    path(
        "add/",
        views.add_department,
        name="add_department"
    ),

    path(
        "view/<int:pk>/",
        views.department_detail,
        name="department_detail"
    ),

    path(
        "edit/<int:pk>/",
        views.edit_department,
        name="edit_department"
    ),

    path(
        "delete/<int:pk>/",
        views.delete_department,
        name="delete_department"
    ),

]