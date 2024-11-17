from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # Your code for creating a book
    return render(request, 'create_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Your code for editing a book
    return render(request, 'edit_book.html', {'book': book})

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Your code for viewing a book
    return render(request, 'view_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Your code for deleting a book
    return render(request, 'delete_book.html', {'book': book})
