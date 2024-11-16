from django.urls import path
from .views import add_book, edit_book, delete_book, list_books, LibraryDetailView  # Import necessary views

urlpatterns = [
    path('books/', list_books, name='list_books'),  # URL for listing books
    path('book/add/', add_book, name='add_book'),  # URL for adding a book
    path('book/<int:pk>/edit/', edit_book, name='edit_book'),  # URL for editing a book
    path('book/<int:pk>/delete/', delete_book, name='delete_book'),  # URL for deleting a book
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for library detail (CBV)
]
