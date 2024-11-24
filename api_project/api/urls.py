from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Initialize the DefaultRouter
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Include the BookList API view
    path('books/', BookList.as_view(), name='book-list'),
    
    # Include all routes registered with the router
    path('', include(router.urls)),
]
