from django import forms
from .models import LibraryBook

class LibraryBookForm(forms.ModelForm):
    class Meta:
        model = LibraryBook
        fields = ['title', 'author', 'publication_year', 'category', 'image']

	

