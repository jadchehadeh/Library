from django.shortcuts import render,redirect,get_object_or_404
from .models import LibraryBook
from .forms import LibraryBookForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib import messages
from django.db.models import Q
from rest_framework import generics
from .serializers import BookSerializer

def about(request):
	return render(request,'about.html')

#def home(request):
	#books = LibraryBook.objects.all()#
	#context={'books':books}#
	#return render(request,'home.html',context)#

class BookListListView(ListView): #Here i use the build in generic view as a parent class to list the books available#
	model=LibraryBook
	template_name='home.html'
	context_object_name='books'
	ordering=['-id']
	paginate_by=3

class BookListListViewNotAuth(ListView):  #this function list the books when the user is not register so he can only view books and will not be able to update or delete a Book that uses a different template#
    model=LibraryBook
    template_name='book_list_not_auth.html'
    context_object_name='books'
    ordering=['-id']
    paginate_by=3

def InsertNewBook(request): #This function responsible for inserting new book into database that uses a build in form provided by django . I make this a function based view for a reason to have differntial in the structure of these view#
    if request.method == 'POST':
        form = LibraryBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,f"Book has been added successfully")
            return redirect('home')  
    else:
        form = LibraryBookForm()
    
    return render(request, 'InsertNewBook.html', {'form': form})



def delete_book(request, book_id):#As it's name tell this function responsible for deleting a book based on its id that is passed as a query string in the url and Uses messages to inform the user that the deleting done successfuly#
    
    book = get_object_or_404(LibraryBook, id=book_id)

    if request.method == 'POST':
       
        book.delete()
        messages.warning(request,f"Book has been deleted successfully")
        return redirect('home')  
    else:
       
        return render(request, 'confirm-delete.html', {'book': book})


class LibraryBookUpdateView(UpdateView): #this is classed based view that uses generic update view for updating a record in database #
    model = LibraryBook  
    form_class = LibraryBookForm  
    template_name = 'book_update.html'
    success_url = '/'  
    def form_valid(self, form):
        messages.success(self.request, 'Book updated successfully.')
        return super().form_valid(form)

#def book_list(request):#
    #books = LibraryBook.objects.all()#
    #return render(request, 'book_list.html', {'books': books})#

def search_books(request):
    query = request.GET.get('q')#This line retrieves the value of the 'q' parameter from the query string of the HTTP request. passed in the get request by the search bar form #
    books = []

    if query:#only is there a text submitted in search bar the query will be performmed . Q string is used here to perform this complex query and to use or | in the query .__icontains responsible to make the search text insensitive#
        books = LibraryBook.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(category__icontains=query)|
            Q(publication_year__icontains=query)
        )

    return render(request, 'search_books.html', {'books': books, 'query': query})

def search_books_not_auth(request): #this function is the same as above but it render different template to avoid un registered user to manage books #
    query = request.GET.get('q')
    books = []

    if query:
        books = LibraryBook.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(category__icontains=query)|
            Q(publication_year__icontains=query)
        )

    return render(request, 'search_books_not_auth.html', {'books': books, 'query': query})    

#Api Working Views#

class BookList(generics.ListCreateAPIView):#This api will retreieve and create a new book in database#
    serializer_class=BookSerializer

    def get_queryset(self):
        queryset=LibraryBook.objects.all()
        title=self.request.query_params.get('title')
        if title is not None:
            queryset=LibraryBook.object.filter(title=title)
        return queryset

class BookDetail(generics.RetrieveAPIView): #retrieve data based on the id #
    queryset = LibraryBook.objects.all()
    serializer_class = BookSerializer

class BookUpdateDelete(generics.RetrieveUpdateDestroyAPIView):#RUD Read Update Delete Api based on the id#
    queryset = LibraryBook.objects.all()
    serializer_class = BookSerializer    
         






