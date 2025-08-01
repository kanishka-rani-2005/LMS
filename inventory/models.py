from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('damaged', 'Damaged'),
        ('lost', 'Lost'),
    ]
    
    code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publisher=models.CharField(max_length=100)
    edition=models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return self.title
