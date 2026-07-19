from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages

from .models import Department
from .forms import DepartmentForm
from django.db.models import Q


# ==========================
# Department List
# ==========================
# ==========================
# Department Detail
# ==========================

def department_detail(request, pk):

    department = get_object_or_404(
        Department,
        pk=pk
    )

    return render(
        request,
        "departments/department_detail.html",
        {
            "department": department
        }
    )
# ==========================
# Department List
# ==========================

def department_list(request):

    search = request.GET.get("search", "")

    departments = Department.objects.all()

    if search:
        departments = departments.filter(
            Q(department_name__icontains=search) |
            Q(department_code__icontains=search) |
            Q(description__icontains=search)
        )

    total_departments = departments.count()

    paginator = Paginator(departments, 15)

    page = request.GET.get("page")

    departments = paginator.get_page(page)

    return render(
        request,
        "departments/department_list.html",
        {
            "departments": departments,
            "search": search,
            "total_departments": total_departments,
        },
    )

# ==========================
# Add Department
# ==========================

def add_department(request):

    if request.method == "POST":

        form = DepartmentForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Department added successfully."
            )

            return redirect("department_list")

    else:

        form = DepartmentForm()

    return render(
        request,
        "departments/add_department.html",
        {
            "form": form
        }
    )


# ==========================
# Edit Department
# ==========================

def edit_department(request, pk):

    department = get_object_or_404(
        Department,
        pk=pk
    )

    if request.method == "POST":

        form = DepartmentForm(
            request.POST,
            instance=department
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Department updated successfully."
            )

            return redirect("department_list")

    else:

        form = DepartmentForm(
            instance=department
        )

    return render(
        request,
        "departments/edit_department.html",
        {
            "form": form
        }
    )


# ==========================
# Delete Department
# ==========================

def delete_department(request, pk):

    department = get_object_or_404(
        Department,
        pk=pk
    )

    department.delete()

    messages.success(
        request,
        "Department deleted successfully."
    )

    return redirect("department_list")



