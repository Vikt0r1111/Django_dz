from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

class PostForm(forms.ModelForm):
    class Meta:
    
        model = Post
        fields = ['title', 'content', 'publication_date', 'author', 'category']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']