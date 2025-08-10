from django.urls import path
from .views import List_view, Book_Detail, add_Book, delete_book

urlpatterns = [
    path("listView/", List_view, name="book_list"),
    path('detail/<int:pk>/', Book_Detail, name='book_detail'),
    path("addBook/", add_Book, name="add_book"),
]

