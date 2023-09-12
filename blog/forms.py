from django import forms
from blog.models import Post, Comments
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'category',
            'text',
            'status_published_post',

        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = (
        'text',
        )