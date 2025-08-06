from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

# Create your views here.


def List_view(request):
    books = Book.objects.filter(Creator=request.user)
    context = {"books": books, 'user': request.user}
    return render(request, 'books/list_books.html', context)


def Book_Detail(requset, id):
    pass


def add_Book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.Creator = request.user
            book.save()
            return redirect('listView')
    elif request.method == "GET":
        form = BookForm()
    return render(request, "books/add_books.html", {"form": form})


def delete_book(request):
    pass
