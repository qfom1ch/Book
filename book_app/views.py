from django.shortcuts import render, get_object_or_404
from .models import Book


def all_book(request):
    Books = Book.objects.order_by('title')
    return render(request, 'book_app/all_book.html',{'Books': Books})


def one_book(request, slug_book):
    book = get_object_or_404(Book, slug=slug_book)
    return render(request, 'book_app/one_book.html',{'book': book})