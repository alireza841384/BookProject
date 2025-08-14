from django.utils import timezone
from django.shortcuts import get_object_or_404, render, redirect
from .models import Book
from .forms import BookForm
from django.db.models import Q

def List_view(request):
    books = Book.objects.filter(Creator=request.user).order_by('-TimeCreated')

    search_query = request.GET.get('search', '').strip()
    search_in = request.GET.get('search_in', 'both')
    date_filter = request.GET.get('date', 'all')

    if search_query:
        if search_in == 'book':
            books = books.filter(BookName__icontains=search_query)
        elif search_in == 'author':
            books = books.filter(Author__icontains=search_query)
        else:  # both
            books = books.filter(
                Q(BookName__icontains=search_query) |
                Q(Author__icontains=search_query)
            )

    today = timezone.localdate()
    if date_filter == 'today':
        books = books.filter(TimeCreated__date=today)
    elif date_filter == 'this_month':
        books = books.filter(TimeCreated__year=today.year, TimeCreated__month=today.month)
  

    context = {
        'books': books,
        'search_query': search_query,
        'search_in': search_in,
        'date_filter': date_filter,
    }
    return render(request, 'books/list_books.html', context)


def Book_Detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})


def add_Book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = Book(
                BookName=form.cleaned_data['BookName'],
                Title=form.cleaned_data['Title'],
                Author=form.cleaned_data['Author'],
                Creator=request.user
            )
            book.save()
            return redirect('book_list')
    elif request.method == "GET":
        form = BookForm()
    return render(request, "books/add_books.html", {"form": form})


def delete_book(request, pk):
    user = request.user
    try:
        targetBook = Book.objects.get(Creator=user, pk=pk)
    except Book.DoesNotExist:
        return redirect('home')
    targetBook.delete()
    return redirect('/home/listView/')
