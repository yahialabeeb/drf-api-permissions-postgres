from django.db import models
from rest_framework import generics
from .serializers import BooksSerializer
from .permissions import IsAuthorOrReadOnly
from .models import Book

class BooksListView(generics.ListCreateAPIView):    
    serializer_class = BooksSerializer
    queryset = Book.objects.all()

class BooksDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BooksSerializer
    queryset = Book.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)
