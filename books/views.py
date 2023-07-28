from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Author, Book
from .serializer import BookSerializer, AuthorSerializer
from .models import Author


# Create your views here.

@api_view()
def book_list(request):
    queryset = Book.objects.all()
    serializer = BookSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view()
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    serializer = BookSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view()
def author_list(request):
    queryset = Author.objects.all()
    serializer = AuthorSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view()
def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    serializer = AuthorSerializer(author)
    return Response(serializer.data, status=status.HTTP_200_OK)


# def welcome(request):
#     query_set = Author.objects.filter(first_name__icontains="ke")
#     return render(request, 'books/welcome.html', {"authors": list(query_set)})
#
#
# def hello(request):
#     return HttpResponse("Hello from book app")
#
#
# def get_books(request, pk):
#     return HttpResponse(pk)
