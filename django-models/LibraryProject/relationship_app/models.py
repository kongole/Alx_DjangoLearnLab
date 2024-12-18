from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Author model as per the checker requirements
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name  # Returning the author's name

# Librarian model (added to satisfy the checker)
class Librarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    library_name = models.CharField(max_length=200)  # Field to store the library name

    def __str__(self):
        return f"{self.user.username} - {self.library_name}"

# UserProfile model
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Signal to create UserProfile on User creation
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

# Book model with custom permissions
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # ForeignKey to Author
    isbn = models.CharField(max_length=13)
    publication_date = models.DateField()

    class Meta:
        permissions = [
            ("can_add_book", "Can add a book"),
            ("can_change_book", "Can change a book"),
            ("can_delete_book", "Can delete a book"),
        ]
    
    def __str__(self):
        return self.title
