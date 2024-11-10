from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view to list all books with their authors
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    context = {
        'books': books,
    }
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view to display details for a specific library with all its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Get all books related to the library
        return context
