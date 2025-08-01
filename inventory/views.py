from django.shortcuts import render

from inventory.models import Book

def all_books(request):
    books = Book.objects.all()
    return render(request, 'inventory/book_list.html', {'books': books})