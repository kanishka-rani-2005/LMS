from django.db import models
from django.contrib.auth.models import User
from inventory.models import Book

class Borrowing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_on = models.DateField(auto_now_add=True)
    returned_on = models.DateField(null=True, blank=True)
    fine = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"


   