from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'book_id': self.id}) 
    # This method returns the URL to access the detail view of a book.
    # It uses Django's reverse function to generate the URL based on the book's ID.