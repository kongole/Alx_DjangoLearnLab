# relationship_app/views.py

from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import DetailView
from .forms import RegisterForm
from .models import Library, Book

# Login view
class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout view
class UserLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# Registration view
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # Redirect to a home page after registration
    else:
        form = RegisterForm()
    return render(request, "relationship_app/register.html", {"form": form})

# Function-based view for listing books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for displaying library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
