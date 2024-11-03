from django import forms
from .models import Author, Book


class BookForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Book
        fields = '__all__'


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
