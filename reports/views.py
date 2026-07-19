from django.http import HttpResponse
from reportlab.pdfgen import canvas

from posts.models import Post, Like, Comment
from departments.models import Department
from django.contrib.auth.models import User
from openpyxl import Workbook


def download_pdf(request):

    response = HttpResponse(content_type="application/pdf")

    response["Content-Disposition"] = 'attachment; filename="Analytics_Report.pdf"'

    p = canvas.Canvas(response)

    p.setFont("Helvetica-Bold", 18)
    p.drawString(180, 800, "Social Media Analytics Report")

    p.setFont("Helvetica", 12)

    y = 750

    p.drawString(50, y, f"Total Users : {User.objects.count()}")
    y -= 30

    p.drawString(50, y, f"Total Posts : {Post.objects.count()}")
    y -= 30

    p.drawString(50, y, f"Total Likes : {Like.objects.count()}")
    y -= 30

    p.drawString(50, y, f"Total Comments : {Comment.objects.count()}")
    y -= 30

    p.drawString(50, y, f"Departments : {Department.objects.count()}")

    p.save()

    return response
def download_excel(request):

    wb = Workbook()

    ws = wb.active

    ws.title = "Analytics Report"

    ws.append(["Category", "Count"])

    ws.append(["Users", User.objects.count()])
    ws.append(["Posts", Post.objects.count()])
    ws.append(["Likes", Like.objects.count()])
    ws.append(["Comments", Comment.objects.count()])
    ws.append(["Departments", Department.objects.count()])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response["Content-Disposition"] = 'attachment; filename="Analytics_Report.xlsx"'

    wb.save(response)

    return response