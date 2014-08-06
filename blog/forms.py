from django.forms import ModelForm
from django import forms

from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]


class CommentsForm(forms.Form):
    name = forms.CharField(max_length=32)
    comment = forms.CharField(widget=forms.Textarea(attrs={'cols': 30,
                                                    'rows': 4}))


class PostForm(forms.Form):
    title = forms.CharField(max_length=50)
    body = forms.CharField(widget=forms.Textarea, required=False)
