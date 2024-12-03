from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'blog'


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:post_pk>/comments/new/', views.CommentCreateView.as_view(), name='add_comment'),
    path('post/<int:post_pk>/comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='edit_comment'),
    path('post/<int:post_pk>/comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete_comment'),
     path('posts/<int:post_pk>/comments/new/', views.CommentCreateView.as_view(), name='add_comment'),
    path('comments/<int:pk>/update/', views.CommentUpdateView.as_view(), name='edit_comment'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete_comment'),
]
