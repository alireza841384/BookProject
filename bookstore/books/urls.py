from django.urls import path
from .views import List_view, Book_Detail, add_Book, delete_book

urlpatterns = [
    path("listView/", List_view),
    path("detail/<int:pk>/", Book_Detail),
    path("addBook/", add_Book),

]
