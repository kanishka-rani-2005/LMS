from django.shortcuts import render, redirect,get_object_or_404
from inventory.models import Book
from borrowing.models import Borrowing
from django.contrib.auth.decorators import login_required
from datetime import date

@login_required
def available_books(request):
    books = Book.objects.filter(status='available')
    return render(request, 'borrowing/available_books.html', {'books': books})


@login_required
def borrow_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if book.status == 'available':
        Borrowing.objects.create(user=request.user, book=book)
        book.status = 'borrowed'
        book.save()
    return redirect('available_books')


@login_required
def return_book(request, borrow_id):
    borrowing = get_object_or_404(Borrowing, id=borrow_id, user=request.user)

    if request.method == 'POST':
        borrowing.returned_on = date.today()
        borrowing.book.status = 'available'
        borrowing.book.save()
        borrowing.save()
        return redirect('my_borrowed_books')

    return render(request, 'borrowing/return_book.html', {'borrowing': borrowing})

@login_required
def my_borrowed_books(request):
    records = Borrowing.objects.filter(user=request.user, returned_on__isnull=True)
    return render(request, 'borrowing/my_books.html', {'records': records})



def calculate_fine(borrowed_on, returned_on):
    allowed_days = 7
    late_days = (returned_on - borrowed_on).days - allowed_days
    return max(0, late_days * 5)


@login_required
def returned_books(request):
    records = Borrowing.objects.filter(user=request.user, returned_on__isnull=False)
    books_with_fines = []

    for record in records:
        fine = calculate_fine(record.borrowed_on, record.returned_on)
        books_with_fines.append({
            'book': record.book,
            'borrowed_on': record.borrowed_on,
            'returned_on': record.returned_on,
            'fine': fine
        })

    return render(request, 'borrowing/returned_books.html', {'books': books_with_fines})