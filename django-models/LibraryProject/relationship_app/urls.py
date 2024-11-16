from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Import views instead of directly importing each view

urlpatterns = [
    # Authentication URLs
    path('register/', views.register, name='register'),  # Register URL mapped to the register view
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Login URL
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Logout URL
    
    # Book-related URLs
    path('books/', views.list_books, name='list_books'),  # URL for listing books
    path('book/add/', views.add_book, name='add_book/'),  # URL for adding a book
    path('book/<int:pk>/edit/', views.edit_book, name='edit_book/'),  # URL for editing a book
    path('book/<int:pk>/delete/', views.delete_book, name='delete_book'),  # URL for deleting a book
    
    # Library-related URLs
    path('library/<int:pk>/', views.library_detail, name='library_detail'),  # URL for library detail
]
