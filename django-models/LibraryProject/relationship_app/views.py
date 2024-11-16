from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .models import Library
from .forms import BookForm

# View to display a list of all books
@login_required
def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# View to add a new book
@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to the list of books
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

# View to edit an existing book
@login_required
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to the list of books
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

# View to delete an existing book
@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to the list of books
    return render(request, 'relationship_app/delete_book.html', {'book': book})

# View to display details of a specific library
@login_required
def library_detail(request, pk):
    library = get_object_or_404(Library, pk=pk)  # Get the library by primary key or return 404
    return render(request, 'relationship_app/library_detail.html', {'library': library})
