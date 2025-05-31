from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Book

# These are function-based views that handle requests and return responses.
def home(request):
    return render(request, 'home.html')

def book_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/detail.html', {'book': book})



# These are class-based views that are more structured for handling CRUD operations and can be reused easily.
class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    # success_url = '/books/' .... no longer needed as we use the get_absolute_url method in the model to redirect to detail page after creation