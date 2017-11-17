from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:  # It tells Django which model should be used to create this form
        model = Post
        fields = ('title', 'text', )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
