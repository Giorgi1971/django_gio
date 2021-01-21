# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from .models import BookModel, AuthorModel
from django.shortcuts import render, get_object_or_404


def index(request):
    lowest_book_list = BookModel.objects.order_by('-quantity')[:7]
    context = {
        'lowest_book_list': lowest_book_list,
    }
    return render(request, 'books/index.html', context)


def book_id(request, book_pk):
    book = get_object_or_404(BookModel, pk=book_pk)
    return render(request, 'books/book_id.html', {'book': book})


def author_id(request, auth_id):
    author = get_object_or_404(AuthorModel, pk=auth_id)
    return render(request, 'books/author_id.html', {'author': author})


def find_author(request, first_letters):
    return HttpResponse("You're voting on question %s." % first_letters)

