from django.urls import path
from .views import BooksListView, BooksDetailView

urlpatterns = [
    
    path('allbooks/', BooksListView.as_view() , name = 'book_list'),
    path('<int:pk>/', BooksDetailView.as_view(), name = 'book_detail') 
]
