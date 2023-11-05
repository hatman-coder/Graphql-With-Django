from django.contrib import admin
from .models import Book, Author

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
