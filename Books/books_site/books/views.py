# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from .models import BookModel
from django.shortcuts import render


def index(request):
    lowest_book_list = BookModel.objects.order_by('-quantity')[:7]
    context = {
        'lowest_book_list': lowest_book_list,
    }
    return render(request, 'books/index.html', context)


def book_id(request, book_pk):
    try:
        book = BookModel.objects.get(pk=book_pk)
    except BookModel.DoesNotExist:
        raise Http404("Books does not exist!")
    return render(request, 'books/book_id.html', {'book': book})


def author_id(request, auth_id):
    response = "You're looking at the results of author %s."
    return HttpResponse(response % auth_id)


def find_author(request, first_letters):
    return HttpResponse("You're voting on question %s." % first_letters)

