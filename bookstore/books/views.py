from django.shortcuts import render
from .models import Book

# Create your views here.


def List_view(request):
    books = Book.objects.filter(Creator=request.user)
    context = {"books": books, 'user': request.user}
    return render(request, 'books/list_books.html', context)


def Book_Detail(requset, id):
    pass


def add_Book(request):
    pass


def delete_book(request):
    pass
