from django.urls import path
from  .views import books_detail, books_list

app_name = 'library'

urlpatterns = [
    path('books_list/', books_list, name='books'),
    path('book_detail/<int:book_id>', books_detail, name='book_detail'),
]
