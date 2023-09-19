from django.db import models

class LibraryBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    image=models.ImageField(blank='True',null='True',upload_to='books_pics')
    def __str__(self):
        return self.title