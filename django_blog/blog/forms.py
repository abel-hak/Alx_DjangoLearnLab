from django import forms
from .models import Post
from .models import Comment
from taggit.forms import TagField


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include tags

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']