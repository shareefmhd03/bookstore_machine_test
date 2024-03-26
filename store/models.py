from django.db import models

# Create your models here.

# Book Model:
# ● Create a Book model with fields for title, author, price,
# quantity_in_stock, genre, and isbn.


class Genre(models.Model):
    genre_title = models.CharField(max_length = 50)
     
    def __str__(self) -> str:
        return str(self.genre_title)
    


class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.IntegerField()
    quantity_in_stock = models.IntegerField()
    genre = models.ForeignKey(Genre,on_delete = models.CASCADE)
    isbn = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return str(self.title)


class Review(models.Model):
    book = models.ForeignKey(Book,on_delete = models.CASCADE,default=None)
    rating  = models.FloatField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return str(self.book.title)