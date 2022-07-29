from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
# Create your views here.

def index(request):
    books = Book.objects.all()
    # return HttpResponse(books)
    return render(request, "book_outlet/index.html", {
        "books": books
    })