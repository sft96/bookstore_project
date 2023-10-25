from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from .models import *

from django.core.paginator import Paginator


def index(request):
    books = Book.objects.all()
    genres = BookGenre.objects.all()
    books_per_page = 6
    paginator = Paginator(books, books_per_page)
    page_number = request.GET.get('page')
    page_books = paginator.get_page(page_number)
    context = {'title': 'Bookstore', 'books': page_books, 'genres': genres}
    return render(request, 'books/index.html', context)


def book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {'book': book}
    return render(request, 'books/book.html', context)


def genre(request, pk):
    book_list = Book.objects.filter(genre=pk)
    book_genre = BookGenre.objects.filter(pk=pk)
    context = {'book_list': book_list, 'book_genre': book_genre}
    return render(request, 'books/genre.html', context)


def basket_add(request, book_id):
    book = Book.objects.get(id=book_id)
    basket = Basket.objects.filter(user=request.user, book=book)
    if not basket.exists():
        Basket.objects.create(user=request.user, book=book, quantity=1)
    else:
        basket = basket.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
