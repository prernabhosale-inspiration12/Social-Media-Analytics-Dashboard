from django.urls import path
from .views import download_pdf, download_excel

urlpatterns = [

    path(
        "pdf/",
        download_pdf,
        name="download_pdf"
    ),

    path(
        "excel/",
        download_excel,
        name="download_excel"
    ),

]