# relationship_app/urls.py

from django.urls import path
from . import views
from .views import UserLoginView, UserLogoutView, register, list_books, LibraryDetailView

urlpatterns = [
    # Authentication views
    path('login/', UserLoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', UserLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    # Book and Library views
    path('books/', views.list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
]
