# relationship_app/urls.py

from django.urls import path
from . import views
from .views import UserLoginView, UserLogoutView, register, list_books, LibraryDetailView

urlpatterns = [
    # Authentication views
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    
    # Book and Library views
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
]
