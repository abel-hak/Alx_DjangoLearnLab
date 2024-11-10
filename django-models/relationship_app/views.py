from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book, Library, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.decorators import user_passes_test


# Register view
class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            return redirect('home')  # Redirect to the home page or another page after registration
        return render(request, 'relationship_app/register.html', {'form': form})


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


# Role-based access views

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'


# Admin view - accessible only to 'Admin' users
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')


# Librarian view - accessible only to 'Librarian' users
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')


# Member view - accessible only to 'Member' users
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')
