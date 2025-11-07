from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'cols': 50,
                'style': 'resize: none;'
            }),
            'author': forms.TextInput(attrs={'size': 30})
        }

    