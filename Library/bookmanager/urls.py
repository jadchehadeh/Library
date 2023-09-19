from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
     path('', views.BookListListView.as_view(), name='home'),#url responsible for listing all books in database #

     path('listbooks/', views.BookListListViewNotAuth.as_view(), name='listbooks'),

    path('about/', views.about, name='about'),

   	path('newbook/',views.InsertNewBook,name='newbook'),

   	 path('delete/<int:book_id>/', views.delete_book, name='delete_book'),

     path('update/<int:pk>/', views.LibraryBookUpdateView.as_view(), name='book_update'),
     
    path('books/search/', views.search_books, name='search_books'),

    path('books/searchnotauth/', views.search_books_not_auth, name='search_books_not'),

   # here are the urls for Handling Api's #
   path('api/listbooks/', views.BookList.as_view(), name='BookList'),

   path('api/books/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),

   path('api/bookmanage/<int:pk>/', views.BookUpdateDelete.as_view(), name='book-update-delete'),
]



