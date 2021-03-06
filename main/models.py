from tabnanny import verbose
from django.db import models

class BooksModel(models.Model):
    name = models.CharField(max_length=256)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'