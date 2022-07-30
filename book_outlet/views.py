from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from .models import Book
from django.db.models import Avg, Max, Min
# Create your views here.

def index(request):
    books = Book.objects.all().order_by("-rating")
    # return HttpResponse(books)
    print("books", list(books))
    num_books = books.count()
    average_rating = books.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html", {
        "books": books,
        "total_number_of_books" : num_books ,
        "average_rating" : average_rating 
    })


def book_detail(request, slug):
    try:
        book = Book.objects.get(slug=slug)
    except:
    #     raise Http404()
    # book = get_object_or_404(Book, pk=id)
        return HttpResponseNotFound("book not found with this id.")
    return render(request, "book_outlet/book_detail.html", {
        "title" : book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller" : book.is_bestselling
    })
