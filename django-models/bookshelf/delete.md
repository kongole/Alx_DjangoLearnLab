from bookshelf.models import Book
book.delete()
Book.objects.all()

# Delete Book Instance
```python
book.delete()
Book.objects.all()
# Expected Output:
# <QuerySet []>
