from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    brief = models.TextField()
    published_year = models.CharField(max_length=4, blank=True, null=True)

    def __str__(self):
        return f'{self.title} ({self.published_year})'