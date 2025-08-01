from django.urls import path
from borrowing.views import available_books, borrow_book, my_borrowed_books, return_book,returned_books

urlpatterns = [
    path('', available_books, name='available_books'),
    path('borrow/<int:book_id>/', borrow_book, name='borrow_book'),
    path('return/<int:borrow_id>/', return_book, name='return_book'),
    path('my-books/', my_borrowed_books, name='my_borrowed_books'),
    path('returned-books/',returned_books, name='returned_books'),

]

