from django.shortcuts import render
from .models import Book, Reader, Issue

def index(request):
    books = Book.objects.all()
    readers = Reader.objects.all()
    issues = Issue.objects.select_related("book", "ticket_number")

    context = {
        "project_name": "Бібліотека",
        "student": "Бачинський Олександр Анатолійович, ІПЗ-22009б",
        "books": books,
        "readers": readers,
        "issues": issues,
    }

    return render(request, "index.html", context)
