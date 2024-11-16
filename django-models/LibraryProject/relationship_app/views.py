from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Library
from .forms import BookForm

# Custom test functions to check user roles
def is_member(user):
    return user.groups.filter(name='Members').exists()

def is_librarian(user):
    return user.groups.filter(name='Librarians').exists()

def is_admin(user):
    return user.is_superuser  # Checks if the user is an admin

# View to handle user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('list_books')  # Redirect to the book list view
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# View to display a list of all books
@login_required
def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# View to add a new book (requires 'can_add_book' permission)
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')  # Redirect to the list of books
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

# View to edit an existing book (requires 'can_change_book' permission)
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')  # Redirect to the list of books
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

# View to delete an existing book (requires 'can_delete_book' permission)
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')  # Redirect to the list of books
    return render(request, 'relationship_app/delete_book.html', {'book': book})

# View to display details of a specific library
@login_required
def library_detail(request, pk):
    library = get_object_or_404(Library, pk=pk)  # Get the library by primary key or return 404
    return render(request, 'relationship_app/library_detail.html', {'library': library})

# User role-based views

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')
