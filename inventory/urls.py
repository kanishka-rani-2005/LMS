from django.urls import path
from inventory.views import all_books

urlpatterns = [
    path('',all_books, name='all_books'),
]