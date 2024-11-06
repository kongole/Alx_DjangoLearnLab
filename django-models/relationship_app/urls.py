from django.urls import path
from . import views

urlpatterns = [
    path('book/add/', views.add_book/, name='add_book'),
    path('book/<int:pk>/edit/', views.edit_book/, name='edit_book'),
    path('book/<int:pk>/delete/', views.delete_book, name='delete_book'),
    # Other URL patterns can be added here as needed
]
