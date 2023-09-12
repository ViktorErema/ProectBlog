from django import forms
from blog.models import Post, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'category',
            'text',
            'status_published_post',

        )
