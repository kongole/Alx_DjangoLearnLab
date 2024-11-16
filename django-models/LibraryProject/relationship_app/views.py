from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Book

# View to display a list of all books
@login_required
def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})
