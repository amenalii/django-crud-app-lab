from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def book_index(request):
    return render(request, 'books/index.html')