from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import list_books

urlpatterns = [
    # Registration view
    path('register/', views.RegisterView.as_view(), name='register'),
    
    # Login view
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    
    # Logout view with a specified template
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    path('books/', views.list_books, name='list_books'),  # Function-based view for listing books
    
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library details
]
